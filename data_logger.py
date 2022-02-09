#!/usr/bin/env python3

import _thread
import time

import minimalmodbus

import PXU

#a = PXU.PXU('COM4', 3)
b = PXU.PXU('COM4', 5)


def print_time(thread_name, delay, id):
    while 1:
        time.sleep(delay)
        pv = 0
        try:
            #if id == 3:
            #    pv = a.read_pv()
            #else:
            pv = b.read_pv()
            print("%s: %s - %s" % (thread_name, time.ctime(time.time()), pv))
        except IOError as e:
            print(e)


try:
    _thread.start_new_thread(print_time, ("Thread-1", 1, 3))
    time.sleep(1)
    _thread.start_new_thread(print_time, ("Thread-2", 1, 5))
except:
    print("Boom")

while 1:
    pass
