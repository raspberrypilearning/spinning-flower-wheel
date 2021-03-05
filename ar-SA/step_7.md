## استخدام زر لبدء تشغيل برنامج الدوران الخاص بك

يتضمن Explorer HAT أيضًا العديد من أزرار الإدخال. دعونا نستخدم الزر لبدء برنامج الزهرة الدوارة أو العجلة عندما تريد ذلك.

- مع فتح برنامج Python الخاص بك، انتقل إلى أعلى `explorerhat.motor.one.forward(100)` وقم بإضافة سطر لتحديد دالة تسمى `run_motor`. بعد ذلك ، قم بتمييز الأسطر الثلاثة من التعليمات البرمجية التي تتحكم في المحرك واضغط على `tab` لتثبيتها. وهي الآن جزء من الوظيفة.
    
    ```python
    def run_motor(channel, event):
      explorerhat.motor.one.forward(100)
      sleep(10)
      explorerhat.motor.one.stop()
    ```

- تحت الدالة الخاصة بك، أضف سطراً من التعليمات البرمجية لإخبار Explorer HAT بتشغيل الدالة عند الضغط على الزر الأول. **لا<0> يجب وضع مسافة بادئة لسطر التعليمات البرمجية هذا. وبدلا من ذلك، ينبغي أن يكون في أقصى اليسار من الصفحة.</p> 
    
    ```python
    explorerhat.touch.one.pressed(run_motor)
    ```</li> 
    
    - حفظ ملف التعليمات البرمجية المعدلة وتشغيلها بالضغط على **F5**. لن يحدث شيء حتى تضغط على الزر الأول في Explorer HAT. لذا جربها: اضغط على هذا الزر!</ul>