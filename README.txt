DUGAIN YOHAN
NARETTO LILIAN

Exécution : python3 generator.py

Pré-requis : Python 3.* et un système 64bits

Le fichier Addition.asm permets de vérifier le bon fonctionnement de notre programme.

Ce programme génère un nouveau fichier assembleur dont la signature n'existe déjà pas dans le payload.txt.
Si la signature a déjà été générée, le programme se chargera de générer un nouveau binaire ayant une signature différente de tous les binaires générés précédemment.

Le fichier ORIGINAL n'est pas modifié, le fichier assembleur FINAL se trouve dans tmp_gen.asm.
Le fichier FINAL s'exécute toujours de cette façon ./tmp_gen.bin

Lors d'une nouvelle génération, les anciens fichiers temporaires (utilisées pour une ancienne génération) sont supprimés.
