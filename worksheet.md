# Make a Digital Landscape of Spinning Flowers & Pinwheels

## Step 1: Connect Pibrella to Raspberry Pi GPIO pins

## Step 2: Connect motor and wheel

## Step 3: Write some code

1. From the command line for an LXTerminal window type `nano spinning-flower.py` and press **Enter** on the keyboard. This will open a blank text editor file in which you can type your code.
1. Begin your code by importing the pibrella python library needed to control the motor by typing 
    
    ```python
    import pibrella
    ```
1. Underneath import the time library in the same way so that you can add time delays to your program:

    ```python
    import time
    ```
1. Leave a blank line of code by pressing enter.
1. Underneath you can now write the sequence of instructions to control the motor attached. 

  ```python
  pibrella.output.e.on()
  time.sleep(10)
  pibrella.output.e.off()
  
  
