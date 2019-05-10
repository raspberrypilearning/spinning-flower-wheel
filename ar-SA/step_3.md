## Attach the Explorer HAT to your Raspberry Pi

- Make sure that your Raspberry Pi is turned off. Connect the Explorer HAT to your Raspberry Pi by pushing it onto the GPIO pins.
    
    ![Explorer HAT mounted on Pi](images/explorer-hat.png)

- Connect the micro USB power supply, and your Raspberry Pi will boot.

- Check you have the Explorer HAT installed correctly by running the following command:

```bash
python3 -c "import explorerhat"
```

If you do not see the messsage `Explorer HAT Pro detected...` then check the Explorer HAT is mounted and that you have entered the command above correctly.