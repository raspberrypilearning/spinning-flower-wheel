## Attacher l'Explorer HAT à ton Raspberry Pi

- Assure-toi que ton Raspberry Pi est éteint. Connecte l'Explorer HAT à ton Raspberry Pi en le poussant sur les broches GPIO.
    
    ![Explorer HAT monté sur Pi](images/explorer-hat.png)

- Connecte l'alimentation micro USB, et ton Raspberry Pi démarrera.

- Vérifie que l'Explorateur HAT est correctement installé en exécutant la commande suivante :

```bash
python3 -c "import explorerhat"
```

Si tu ne vois pas le message `Explorer HAT Pro détecté...` alors vérifie que l'Explorer HAT est monté et que tu as entré la commande ci-dessus correctement.