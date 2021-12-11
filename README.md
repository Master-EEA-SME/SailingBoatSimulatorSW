# Simulateur
## Requirements
Vérifiez que vous avez Python 3 installé. Pour cela ouvrez un terminal et lancez la commande suivante :
```sh
$ python --version
Python 3.9.6
```
Si la commande vous affiche la version de python cela veut dire que python est installé. Vérifiez bien que c'est python 3 qui est installé grâce au premier chiffre qui apparaît (Python 3.X.Y).
### Installation de Python
Installer sur votre machine Python 3.
#### Ubuntu
```sh
$ sudo apt-get install python3
```
#### Windows
Si vous êtes sur Windows 10, lorsque vous avez tapé **python --version**, windows a du vous ouvrir le **Microsoft Store** pour installer Python. Vous pouvez installer Python à partir du Microsoft Store. Sinon cliquez et installez Python en allant sur le site officiel de [Python](https://www.python.org/downloads/).

#### Mac OS
Installez Python en allant sur le site officiel de [Python](https://www.python.org/downloads/).

Après avoir installé Python réessayez la commande suivante :
```sh
$ python --version
Python 3.9.6
```
Si la commande vous affiche la version de Python cela veut dire que Python est bien installé.
### pip
Vérifiez que **pip** est bien installé grâce à la commande suivante :
```sh
$ python -m pip --version
pip 21.2.4 ...
```
Si la commande vous affiche la version de **pip** cela veut dire que pip est bien installé. Sinon tapez la commande suivante :
```sh
$ python -m ensurepip --default-pip
```
Et ensuite :
```sh
$ python -m pip install --upgrade pip setuptools wheel
```

### Installation des dépendances
Avant de lancer le simulateur installez les libraires suivantes en utilisant **pip**.
```sh
$ python -m pip install PySide6 PySerial
```

## Execution
Pour lancer le simulateur ouvrez un terminal et placez vous dans le dossier où ce **README.md** se trouve et lancez la commande suivante :
```sh
$ python main.py
``` 