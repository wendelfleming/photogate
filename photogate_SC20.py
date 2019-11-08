#!/usr/bin/env python3
"""
"""
import logging
from gpiozero import DigitalInputDevice
import time
import math
import argparse

class Photogate_SC20(object):
    def __init__(self, gate0_pin: int, gate1_pin: int, gate_distance: float, pin_factory = None):
        """
        :type gate0_pin: None
        :type gate1_pin: None
        :type gate_distance: Float
        """
        logging.info('Initializing a photogate.')
        self._gate_0 = DigitalInputDevice(gate0_pin, pin_factory = pin_factory)
        self._gate_1 = DigitalInputDevice(gate1_pin, pin_factory = pin_factory)
        self._gate_distance = gate_distance
        self._gate_0_trigger_time = float('nan')
        self._gate_1_trigger_time = float('nan')
        _gate_0.when_deactivated = self._trigger_gate_0
        _gate_1.when_deactivated = self._trigger_gate_1
        
    def _trigger_gate_0(self):
        self._gate_0_trigger_time = time()
    
    def _trigger_gate_1(self):
        return self._gate_1_trigger_time = time()
        
    def reset(self):
        self._gate_0_trigger_time = float('nan')
        self._gate_1_trigger_time = float('nan')
    
    def get_gate_0_trigger_time(self):
        return _gate_0_trigger_time
    
    def get_gate_1_trigger_time(self):
        return _gate_1_trigger_time
    
    def get_gate_distance(self):
        return self._gate_distance
    
    def get_speed(self):
        if math.isnan(_gate_0_trigger_time) or math.isnan(_gate_1_trigger_time):
            return float('nan')
        else:
            return self._gate_distance/(self._gate_1_trigger_time - self._gate_0_trigger_time)
    
    def measure_speed(self):
        self._gate_0.wait_for_inactive()
        self._gate_1.wait_for_inactive()
        return self.get_speed()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Runs the photogate to determine the speed of "
                    "an object that passes through the photogate.")
    parser.add_argument("-p0", dest="pin1", default=7, type=int,
                        help="GPIO pin of the photogate's gate 0")
    parser.add_argument("-p1", dest="pin1", default=7, type=int,
                        help="GPIO pin of the photogate's gate 1")
    args = vars(parser.parse_args())

    encoder = OptocouplerEncoder(gpio_pin=args['pin'])
    previous_rotations = encoder.get_rotations()
    print("Waiting for the encoder to turn...")
    while True:
        rotations = encoder.get_rotations()
        if rotations != previous_rotations:
            previous_rotations = rotations
            print("Rotations:     {:f}".format(rotations))
            print("Rotation Rate: {:f}".format(encoder.get_rotation_rate()))
            print("Waiting for the encoder to turn...")
        time.sleep(0.1)
