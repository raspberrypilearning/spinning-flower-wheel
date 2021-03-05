## أرفاق Explorer HAT بـ Raspberry Pi الخاص بك

- تأكد من إيقاف تشغيل Raspberry Pi. قم بتوصيل Explorer HAT بـ Raspberry Pi الخاص بك عن طريق دفعه الى دبابيس GPIO.
    
    ![تم تثبيت Explorer HAT على Pi](images/explorer-hat.png)

- قم بتوصيل مصدر طاقة USB الصغيرة وسيتم تشغيل Raspberry Pi الخاص بك.

- تحقق من تثبيت Explorer HAT بشكل صحيح عن طريق تشغيل الأمر التالي:

```bash
python3 -c "import explorerhat"
```

إذا كنت لا ترى الرسالة `Explorer HAT Pro تم اكتشافها...` فتحقق من تثبيت Explorer HAT وأنك أدخلت الأمر أعلاه بشكل صحيح.