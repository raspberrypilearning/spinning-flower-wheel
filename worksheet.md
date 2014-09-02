# Make a Digital Landscape of Spinning Flowers & Pinwheels

## Step 1: Connect Pibrella to Raspberry Pi GPIO pins

## Step 2: Prepare your motor and wheel
It is likely that your motors and wheels have been supplied seperately and therefore need to be connected in order for you to use them. *Note: You may need to ask a responsible adult for some help in this step.*

1. Place the foam wheel on a desk, ensuring that you have placed some cardboard or newspaper unerneath to protect the table.
1. Put a small amount of strong glue into the hole in the centre of the wheel.
1. Push the shaft of your motor into the hole, ensuring that you do not push it all the way to the bottom (half way should do) and hold it as straight as possible whilst the glue sets. 
1. Next, take two male to male jumper cables and snip off one end. Using some wire strippers expose a small amount of the cable underneath.
1. Solder the wire ends to the opposite end of the motor to the wheel, where there are two small metal prongs. 
1. Once the solder has hardened, take a paper or plastic cup and using some scissors or a sharp pencil make a hole in the middle, just a little smaller than the size of the motor. 
1. Push your motor into the hole in the cup, so that the wheel sticks out of the buttom, and the jumper wires come out of the top. 1. Turn your cup upside down on the table and connect the two jumper wires to your pibrella board.

## Step 3: Write code to make the motor turn

1. From the command line for an LXTerminal window type `nano spinning-wheel.py` and press **Enter** on the keyboard. This will open a blank text editor file in which you can type your code.
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
  ```
  
1. Press **CTRL** and **X** on the keyboard, followed by **Y** to save your code.
1. Run your program by typing `sudo python spinning-wheel.py`.
