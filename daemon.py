import logging
logging.basicConfig(level=logging.DEBUG)



from slack_bolt.app.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler

import os
import json
import serial

ARDUINO_DEVICE_PATH = '/dev/ttyACM0'
BAUDRATE = 9600

app = AsyncApp(token=os.environ['BOT_TOKEN'])

SLACK_STATUS_API_ENDPOINT = 'https://slack.com/api/users.profile.set'
SLACK_MESSAGE_API_ENDPOINT = 'https://slack.com/api/chat.postMessage'


async def main():
    # ser = serial.Serial(ARDUINO_DEVICE_PATH, BAUDRATE, timeout=0)
    # while(ser.isOpen()):
    #    if (ser.in_waiting > 0):
    #        data = ser.read(ser.in_waiting)
    # pass
    handler = AsyncSocketModeHandler(app, os.environ['WS_TOKEN'])
    await handler.start_async()

@app.event("app_mention")
async def event_test(body, say, logger):
    logger.info(body)
    await say("What's up?")

@app.command("/hello-bolt-python")
async def command(ack, body, respond):
    await ack()
    await respond(f"Hi <@{body['user_id']}>!")

if __name__ == '__main__':
    import asyncio
    
    asyncio.run(main())