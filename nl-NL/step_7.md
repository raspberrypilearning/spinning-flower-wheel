## Gebruik een knop om je draaiprogramma te starten

De Explorer HAT bevat ook verschillende invoerknoppen. Laten we een knop gebruiken om e draaiende bloem- of windmolen-programma te starten wanneer jij dat wilt.

- Open het Python-programma en ga naar net boven `explorerhat.motor.one.forward (100)` en voeg een regel toe om een ​​functie met de naam `run_motor` te definiëren. Markeer vervolgens de drie coderegels die de motor besturen en druk op de `tab` toets om ze in te laten springen. Ze maken nu deel uit van de functie.
    
    ```python
    def run_motor(channel, event):
    explorerhat.motor.one.forward(100)
    sleep(10)
    explorerhat.motor.one.stop()
    ```

- Voeg onder je functie een regel code toe om de Explorer HAT de opdracht te geven om de functie uit te voeren wanneer knop één wordt ingedrukt. Deze coderegel moet **niet** ingesprongen zijn. In plaats daarvan moet het helemaal links op de pagina staan.
    
    ```python
    explorerhat.touch.one.pressed(run_motor)
    ```

- Sla het gewijzigde codebestand op en voer het uit door op **F5** drukken. Er gebeurt niets totdat je op knop één van de Explorer-HAT drukt. Dus probeer het eens: druk op die knop!