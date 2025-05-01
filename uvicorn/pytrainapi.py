from contextlib import asynccontextmanager
import asyncio
from bleak import BleakScanner, BleakClient
from fastapi import FastAPI

HUB_NAME = "mel-train"


UUID="FEC09AEA-C625-307E-FF85-E5BC2A0BF624"
# configure bleak
UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

def hub_filter(device, ad):
    return device.name and device.name.lower() == HUB_NAME.lower()

def handle_disconnect(_):
    print("Hub was disconnected.")

    # If the hub disconnects before this program is done,
    # cancel this program so it doesn't get stuck waiting
    # forever.

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
        self.lights = False
        pass

    async def connect(self):
        # Tell user to start program on the hub.
        print("Start the program on the hub now with the button.")
        device = await BleakScanner.find_device_by_filter(hub_filter)
        self.client = BleakClient(device, disconnected_callback=handle_disconnect)
        await self.client.connect()
        #if self.client.is_connected:
        #    print("Connected")
        await self.client.start_notify(UART_TX_CHAR_UUID, handle_rx)
        #self.nus = self.client.services.get_service(UART_SERVICE_UUID)
        #self.rx_char = self.nus.get_characteristic(UART_RX_CHAR_UUID)
        #print(self.rx_char)

        #print(f"Characteristic {self.rx_char.uuid} has properties: {self.rx_char.properties}")
        # Check if writing is allowed
        #if 'write' in self.rx_char.properties or 'write-without-response' in self.rx_char.properties:
            #print("Characteristic is writable.")
        #else:
            #print("Characteristic is not writable.")

        await self.send(b"fwd")


    async def send(self, data):
        try:
            await self.client.write_gatt_char(UART_RX_CHAR_UUID, b"\x06" + data, response=True)
        except Exception as e:
            # Handle exceptions.
            print(e)


    async def disconnect(self):
        await self.send(b"d")
        await self.send(b"b")
        await self.client.disconnect()

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

@app.get("/disconnect")
async def root():
    await trainClient.disconnect()
    return {"message": "Disconnected"}

@app.get("/accelerate")
async def root():
    await trainClient.send(b"fwd")
    await asyncio.sleep(8)
    return {"message": "Accelerate"}


@app.get("/reverse")
async def root():
    await trainClient.send(b"rev")
    await asyncio.sleep(9)
    return {"message": "Go in reverse"}

@app.get("/stop")
async def root():
    await trainClient.send(b"bye")
    return {"message": "Stop"}

@app.get("/lap")
async def root():
    lights = await trainClient.send(b"l")
    return {"message": "do a lap of the track"}


