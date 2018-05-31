#!/usr/bin/env python

'''Farmware: execute a set_pin_io_mode command.'''

import os
import sys
import json
import requests

farmware_name = 'set_pin_io_mode'

def get_env(key, type_=int):
    return type_(os.environ['{}_{}'.format(farmware_name, key)])

pin_number = get_env('pin_number')
pin_io_mode = get_env('pin_io_mode')

def send(cs):
    '''Send a celery script command.'''
    return requests.post(
        os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
        headers={'Authorization': 'Bearer ' + os.environ['FARMWARE_TOKEN'],
                 'content-type': 'application/json'},
        data=json.dumps(cs))

def set(pin_number, pin_io_mode):
    '''Send a set_pin_io_mode command to set a pin's to the Web App.'''
    kind = 'set_pin_io_mode'
    response = send({
        'kind': kind,
        'args': {
            'pin_number': pin_number,
            'pin_io_mode': pin_io_mode}})
    if response.status_code != 200:
        print(response.status_code)
        print(json.dumps({
        'kind': kind,
        'args': {
            'pin_number': pin_number,
            'pin_io_mode': pin_io_mode}}))
        message = 'Invalid Farmware CeleryScript: `{}` ({}).'.format(
            kind, response.status_code)
        send({
            'kind': 'send_message',
            'args': {
                'message': message,
                'message_type': 'error'}})
        sys.exit(1)

if __name__ == '__main__':
    set(pin_number, pin_io_mode)
