## Bevestig de Explorer HAT aan je Raspberry Pi

- Zorg ervoor dat je Raspberry Pi is uitgeschakeld. Verbind de Explorer HAT met je Raspberry Pi door deze op de GPIO-pinnen te duwen.
    
    ![Explorer HAT mounted on Pi](images/explorer-hat.png)

- Sluit de micro USB-voeding aan en de Raspberry Pi start op.

- Controleer of de Explorer HAT correct is geïnstalleerd door de volgende opdracht uit te voeren:

```bash
python3 -c "import explorerhat"
```

Als je het bericht `Explorer HAT Pro detected...` niet ziet, controleer dan of de Explorer HAT is gemonteerd en of je de bovenstaande opdracht correct hebt ingevoerd.