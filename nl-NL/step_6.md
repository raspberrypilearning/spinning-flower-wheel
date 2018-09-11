## Write code to make the motor turn

Once the wheel and motors have been assembled and attached to the Explorer HAT, it is time to program them to do what they were built for... turning!

- From the `Programming` menu, open `Python 3 (IDLE)`
    
    ![Open Python](images/python3-app-menu.png)

- Click **File** > **New File** to create a blank file.

- Begin your code by importing the Explorer HAT Python library needed to control the motor by typing:
    
    ```python
    import explorerhat
    ```

- Underneath that, import the sleep function from the `time` library so that you can add time delays to your program:
    
    ```python
    from time import sleep
    ```

- Now add the sequence of instructions to control the attached motor:
    
    ```python
    explorerhat.motor.one.forward(100)
    sleep(10)
    explorerhat.motor.one.stop()
    ```

- Save your code and run the program by pressing **F5** on the keyboard. Your program should turn the motor on, which will spin the shaft connected to the wheel for ten seconds. How could you make it spin for longer?