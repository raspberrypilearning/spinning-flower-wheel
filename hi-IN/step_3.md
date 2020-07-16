## एक्स्प्लोरर हैट (Explorer HAT) को अपने Raspberry Pi से जोड़े

- ध्यान रखे की आपका Raspberry Pi बंद हो। एक्स्प्लोरर हैट (Explorer HAT) को GPIO पिंस में लगाकर अपने Raspberry Pi से जोड़े।
    
    ![Raspberry Pi पर माउंट (mount) हुआ एक्स्प्लोरर हैट (Explorer HAT) ](images/explorer-hat.png)

- माइक्रो USB ऊर्जा आपूर्ति जोडे, और आपका Raspberry Pi चालू हो जाएगा।

- निम्न कमांड Run करके जाँचें कि आपका एक्स्प्लोरर हैट (Explorer HAT) सही ढंग से इनस्टॉल हुआ है या नहीं:

```bash
python3 -c "import explorerhat"
```

यदि आपको यह मेसेजेज नहीं दिख रहा है कि `Explorer HAT Pro detected...` तो जाँच करे कि एक्स्प्लोरर हैट (Explorer HAT) माउंट (mount) है या नहीं और आपने सही ढंग से ऊपर का कमांड दर्ज किया है या नहीं।