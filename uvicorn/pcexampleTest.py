# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Henrik Blidh
# Copyright (c) 2022-2023 The Pybricks Authors

"""
Example program for computer-to-hub communication.

Requires Pybricks firmware >= 3.3.0.
"""

import asyncio
from contextlib import suppress, asynccontextmanager
from bleak import BleakScanner, BleakClient
from fastapi import FastAPI

PYBRICKS_COMMAND_EVENT_CHAR_UUID = "c5f50002-8280-46da-89f4-6d8051e4aeef"

# Replace this with the name of your hub if you changed
# it when installing the Pybricks firmware.
HUB_NAME = "mel-train"

# async def main():
main_task = asyncio.current_task()

def handle_disconnect(_):
    print("Hub was disconnected.")

    # If the hub disconnects before this program is done,
    # cancel this program so it doesn't get stuck waiting
    # forever.
    if not main_task.done():
        main_task.cancel()

ready_event = asyncio.Event()

def handle_rx(_, data: bytearray):
    if data[0] == 0x01:  # "write stdout" event (0x01)
        payload = data[1:]

        if payload == b"rdy":
            ready_event.set()
        else:
            print("Received:", payload)

class LegoHubClient:
    def __init__(self):
        self.client = None
        #self.ready_event = asyncio.Event()
        self.connected = False

    async def connect(self):
        print("Scanning for LEGO hub...")
        device = await BleakScanner.find_device_by_name(HUB_NAME)
        if device is None:
            raise RuntimeError(f"Could not find hub with name: {HUB_NAME}")

        self.client = BleakClient(device, disconnected_callback=handle_disconnect)
        await self.client.connect()
        print("Connected to hub.")

        await self.client.start_notify(PYBRICKS_COMMAND_EVENT_CHAR_UUID, handle_rx, response=True)
        self.connected = True

        # Tell user to start program on the hub.
        print("Start the program on the hub now with the button.")

    async def disconnect(self):
        print("Disconnecting...")
        await self.send(b"bye")
        self.client.disconnect()
        self.connected = False


    async def send(self, data: bytes):
        if not self.connected or self.client is None:
            raise RuntimeError("LEGO hub is not connected.")

        await self.client.write_gatt_char(
            PYBRICKS_COMMAND_EVENT_CHAR_UUID,
            b"\x06" + data,  # 0x06 = "stdin write" command
            response=True
        )
        print(f"Sent: {data}")

trainClient = LegoHubClient()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await trainClient.connect()
    yield
    await trainClient.disconnect()

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/accelerate")
async def root():
    print("accelerate")
    await trainClient.send(b"fwd")
    return {"message": "Accelerate"}


@app.get("/reverse")
async def root():
    await trainClient.send(b"rev")
    return {"message": "Go in reverse"}

@app.get("/stop")
async def root():
    await trainClient.send(b"stp")
    return {"message": "Stop"}

@app.get("/lap")
async def root():
    await trainClient.send(b"lap")
    return {"message": "do a lap"}


