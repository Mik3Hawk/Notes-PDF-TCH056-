# Automatisation de la capture d'écran et création de PDF

-Par [Noah Tremblay](https://github.com/Mik3Hawk), Janvier 2024

Ce script Python utilise Selenium pour automatiser la capture d'écran d'un site Web et ReportLab pour créer un PDF à partir des captures d'écran. Il est conçu pour prendre des captures d'écran jusqu'à ce que deux captures successives soient identiques.

## Comment ça marche

1. **Initialisation :** Le script ouvre un navigateur Chrome et accède à l'URL spécifié.

2. **Capture d'écran :** Il simule un clic en bas à droite de l'écran pour déclencher une capture d'écran.

3. **Vérification :** Il compare chaque nouvelle capture d'écran à la précédente. La boucle s'arrête lorsque deux captures successives sont identiques.

4. **Conversion en PDF :** Les captures d'écran sont converties en un fichier PDF, deux par page.

## Comment utiliser

### Installation

1. Assurez-vous d'avoir [Python](https://www.python.org/) installé sur votre système.

2. Installez les modules Python requis en exécutant les commandes suivantes dans votre terminal ou invite de commandes :

   ```bash
   pip install selenium
   pip install Pillow
   pip install reportlab

