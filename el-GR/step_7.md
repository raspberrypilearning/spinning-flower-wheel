## Using a button to start your spinning program

The Explorer HAT also includes several input buttons. Let's use a button to start your spinning flower or pinwheel program when you want it to.

- With your Python program open, navigate to just above `explorerhat.motor.one.forward(100)` and add a line to define a function called `run_motor`. Then, highlight the three lines of code which control the motor and press the `tab` key to indent them. They are now part of the function.
    
    ```python
    def run_motor(channel, event):
      explorerhat.motor.one.forward(100)
      sleep(10)
      explorerhat.motor.one.stop()
    ```

- Underneath your function, add a line of code to tell the Explorer HAT to run the function when button one is pressed. This line of code should **not** be indented. Instead, it should be on the far left of the page.
    
    ```python
    explorerhat.touch.one.pressed(run_motor)
    ```

- Save the amended code file and run it by pressing **F5**. Nothing will happen until you press button one on the Explorer HAT. So give it a go: press that button!