## Utiliser un bouton pour démarrer ton programme de rotation

L'Explorateur HAT comprend également plusieurs boutons d'entrée. Utilisons un bouton pour démarrer ton programme de fleur tournante ou moulin à vent quand tu le souhaites.

- Avec ton programme Python ouvert, va au-dessus de `explorerhat.motor.one.forward(100)` et ajoute une ligne pour définir une fonction appelée `run_motor`. Ensuite, mets en surbrillance les trois lignes de code qui contrôlent le moteur et appuie sur la touche `tabulation` pour les indenter. Elles font désormais partie de la fonction.
    
    ```python
    def run_motor(channel, event):
      explorerhat.motor.one.forward(100)
      sleep(10)
      explorerhat.motor.one.stop()
    ```

- Sous ta fonction, ajoute une ligne de code pour dire à l'Explorateur HAT d'exécuter la fonction quand le bouton est appuyé. Cette ligne de code ne doit **pas** être indentée. Au lieu de cela, elle devrait se trouver à l'extrême gauche de la page.
    
    ```python
    explorerhat.touch.one.pressed(run_motor)
    ```

- Enregistre le fichier de code modifié et exécute-le en appuyant sur **F5**. Rien ne se passera tant que tu n'appuieras pas sur un bouton de l'Explorer HAT. Alors donne-lui un coup de main : appuie sur ce bouton !