import pibrella
import time

def turn():
  while True:
    pibrella.output.e.on()
    pibrella.output.e.off()
    time.sleep(0.01)
    if not pibrella.button.read():
      break

while True:
  if pibrella.button.read():
    turn()
