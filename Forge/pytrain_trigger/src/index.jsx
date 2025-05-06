
import { fetch } from '@forge/api'

export async function run(event, context) {
  const doneID = 10038;
  //console.log(event);
  for (let i = 0; i < event.changelog.items.length; i++) {
    if((event.changelog.items[i].field == 'status') && (event.changelog.items[i].to == doneID)) {
      const url = "https://mpaisley-e7cd1e933dfd.public.atlastunnel.com/lap"
      const response = await fetch(url, { method: 'GET' });
      if(!response.ok) {
        const errmsg = `Error from Pytrain API: ${response.status} ${await response.text()}`;
        console.error(errmsg)
        throw new Error(errmsg)
      }
      const message = await response.json();

      console.log(message.message)
    } else if (event.changelog.items[i].field == 'status') {
      console.log('Check for status ID here:');
      console.log(event.changelog.items[i]);
    }
  }
}