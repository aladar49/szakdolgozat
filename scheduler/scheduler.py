import json
import requests
import validators
from random import uniform
from time import sleep

converter_service_unit = 'http://127.0.0.1:8080/convert'

def send_to_converter(data):
    headers = {'Content-type': 'application/json'}
    data_json = json.dumps(data)
    success = False
    while not success:
        response = requests.post(converter_service_unit, data=data_json, headers=headers)
        print(str(response.status_code) + '  ' + response.text)
        if response.status_code == 200:
            success = True
        sleep(5)

def start_load():
    with open('yt_links.txt', 'r') as f:
        for line in f:
            if not validators.url(line):
                break
            data = {'yt_link' : line }
            sleep(uniform(1, 10))
            send_to_converter(data)
            
if __name__ == '__main__':
    start_load()
