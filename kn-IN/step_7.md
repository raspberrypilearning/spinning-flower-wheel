## ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂ ಅನ್ನು ಪ್ರಾರಂಭಿಸಲು ಬಟನ್ (button) ಬಳಸಿ

Explorer HAT ಹಲವಾರು ಇನ್‌ಪುಟ್ ಬಟನ್ (input button)‌ಗಳನ್ನೂ ಒಳಗೊಂಡಿದೆ. ನಿಮ್ಮ ಹೂವು ಅಥವಾ ಪಿನ್‌ವೀಲ್ ಪ್ರೋಗ್ರಾಂ ಅನ್ನು ನೀವು ಬಯಸಿದಾಗ ಪ್ರಾರಂಭಿಸಲು ಬಟನ್ ಬಳಸೋಣ.

- ನಿಮ್ಮ Python ಪ್ರೋಗ್ರಾಂನಲ್ಲಿ `explorerhat.motor.one.forward(100)` ಎಂಬ ಸಾಲನ್ನು ಹುಡುಕಿ, ಅದರ ಮೇಲಿನ ಸಾಲಿನಲ್ಲಿ `run_motor` ಎಂಬ functionನ್ನಿನ ಸಾಲು ಬರುವಂತೆ ಸೇರಿಸಿ. ನಂತರ, ಮೋಟರ್ ಅನ್ನು ನಿಯಂತ್ರಿಸುವ ಮೂರು ಸಾಲುಗಳ ಕೋಡ್ ಅನ್ನು ಹೈಲೈಟ್ ಮಾಡಿ ಮತ್ತು ಅವುಗಳನ್ನು ಇಂಡೆಂಟ್ ಮಾಡಲು `tab` ಕೀ ಒತ್ತಿ. ಈ ಮೂರು ಸಾಲುಗಳು ಈಗ functionನ್ನಿನ ಭಾಗವಾಗುತ್ತವೆ.
    
    ```python
    def run_motor(channel, event):
      explorerhat.motor.one.forward(100)
      sleep(10)
      explorerhat.motor.one.stop()
    ```

- Button one ಒತ್ತಿದಾಗ, Explorer HAT ಈ function ಅನ್ನು run ಮಾಡಲು, functionನ್ನಿನ ಕೆಳಗೆ ಒಂದು ಸಾಲಿನ ಕೋಡ್ ಸೇರಿಸಿ. ಈ ಕೋಡ್‌ (code) ನ ಸಾಲನ್ನು indent **ಮಾಡಬಾರದು**. ಬದಲಾಗಿ, ಅದು ಪುಟದ ಎಡಭಾಗದಲ್ಲಿರಬೇಕು.
    
    ```python
    explorerhat.touch.one.pressed(run_motor)
    ```

- ತಿದ್ದುಪಡಿ ಮಾಡಿದ ಕೋಡ್ (code) ಫೈಲ್ ಅನ್ನು ಸೇವ್ ಮಾಡಿ ಮತ್ತು **F5** ಒತ್ತುವ ಮೂಲಕ ಅದನ್ನು ಚಲಾಯಿಸಿ (run). Explorer HAT‌ನಲ್ಲಿ ನೀವು button one ಅನ್ನು ಒತ್ತುವವರೆಗೂ ಏನೂ ಆಗುವುದಿಲ್ಲ. ಆ button ಅನ್ನು ಒತ್ತಿ: ಎನಾಗುವುದೆಂದು ನೋಡಿ!