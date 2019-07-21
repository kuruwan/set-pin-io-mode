#!/usr/bin/env python

'''Farmware: execute a set_pin_io_mode command.'''

from farmware_tools import get_config_value, device

farmware_name = 'Set pin IO mode-kuruwan'

pin_number = get_config_value(farmware_name, config_name='pin_number')
pin_io_mode = get_config_value(farmware_name, config_name='pin_io_mode')

device.set_pin_io_mode(pin_io_mode, pin_number)
