import explorerhat
from time import sleep

def run_motor(channel, event):
  explorerhat.motor.one.forward(100)
  sleep(10)
  explorerhat.motor.one.stop()

explorerhat.touch.one.pressed(run_motor)
