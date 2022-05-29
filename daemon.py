import os
import json
import requests
import serial


ARDUINO_DEVICE_PATH = '/dev/ttyACM0'
BAUDRATE = 9600

BOT_TOKEN = os.environ['BOT_TOKEN']
USER_TOKEN = os.environ['USER_TOKEN']

BOT_HEADERS = {'Authorization': 'Bearer ' + BOT_TOKEN,
               'Content-Type': 'application/json; charset=utf-8'}

USER_HEADERS = {'Authorization': 'Bearer ' + USER_TOKEN,
               'Content-Type': 'application/json; charset=utf-8'}

SLACK_STATUS_API_ENDPOINT = 'https://slack.com/api/users.profile.set'
SLACK_MESSAGE_API_ENDPOINT = 'https://slack.com/api/chat.postMessage'

SUNNY_EMOJI = ':sunny:'
RAINY_EMOJI = ':cloud_rain:'
CLOUDY_EMOJI = ':cloud:'

VALID_INPUT = ['0', '1', '2']


def main():
    ser = serial.Serial(ARDUINO_DEVICE_PATH, BAUDRATE, timeout=0)
    oldStatus = 0
    while True:
        if ser.in_waiting > 0:
            s = ser.read().decode('utf-8')
            if s in VALID_INPUT:
                currentStatus = int(s)
                if currentStatus != oldStatus:
                    oldStatus = currentStatus
                    change_status(currentStatus)
                    send_message(currentStatus)
            

def send_message(s: int):
    s = "it's raining" if s >= 2 else "now it's sunny" if s <= 0 else "it's cloudy"
    payload = {
        "channel": "C03HAES6HFX",
        "text": s
    }
    requests.post(SLACK_MESSAGE_API_ENDPOINT, data=json.dumps(payload),
                      headers=BOT_HEADERS)


def change_status(s: int):
    payload = {
        'profile': {
            "status_text": "now in Tokyo",
            "status_emoji": RAINY_EMOJI if s >= 2 else SUNNY_EMOJI if s <= 0 else CLOUDY_EMOJI,
            "status_expiration": 0
        }
    }
    requests.post(SLACK_STATUS_API_ENDPOINT, data=json.dumps(payload),
                      headers=USER_HEADERS)


if __name__ == '__main__':
    main()