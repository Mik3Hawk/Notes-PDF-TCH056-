# Importation des modules nécessaires
import time
import pyautogui
from PIL import Image
from selenium import webdriver
from reportlab.pdfgen import canvas

def prendre_screenshot(url, nom_fichier, nombre_max_screenshots=100, output_pdf='output.pdf'):
    # Initialisation du navigateur Chrome
    navigateur = webdriver.Chrome(options=webdriver.ChromeOptions())

    try:
        # Accès à l'URL spécifiée
        navigateur.get(url)
        navigateur.implicitly_wait(5)
        captures = []

        # Boucle pour prendre des captures d'écran jusqu'à atteindre le nombre maximum ou détecter une capture identique
        for i in range(1, nombre_max_screenshots + 1):
            navigateur.save_screenshot(nom_fichier.format(i))
            captures.append(nom_fichier.format(i))

            # Vérification si la capture actuelle est identique à la précédente
            if i > 1 and Image.open(captures[-1]) == Image.open(captures[-2]):
                print(f"Les captures {captures[-1]} et {captures[-2]} sont identiques. Arrêt de la boucle.")
                break

            # Simuler un clic en bas à droite de l'écran avec pyautogui
            largeur_ecran, hauteur_ecran = pyautogui.size()
            pyautogui.click(largeur_ecran - 650, hauteur_ecran - 140) #À MODIFIER
                # Modifiez les dimensions x,y jusqu'à ce que votre curseur soit sur la flèche droite en bas de l'écran

            # Pause entre chaque capture d'écran
            time.sleep(0.5)

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

    finally:
        # Fermeture du navigateur
        navigateur.quit()
        # Conversion des captures en un fichier PDF
        images_to_pdf(captures, output_pdf)

def images_to_pdf(images, output_pdf):
    # Initialisation du canvas PDF avec les dimensions de l'écran
    pdf = canvas.Canvas(output_pdf, pagesize=(pyautogui.size()[1], pyautogui.size()[0]))

    # Boucle pour ajouter les images au PDF, deux par page
    for i in range(0, len(images), 2):
        pdf.showPage()
        draw_image(pdf, images[i], 0, 0)

        # Ajout de la deuxième image si disponible
        if i + 1 < len(images):
            draw_image(pdf, images[i + 1], 0, calculate_height(images[i]))

    # Enregistrement du PDF final
    pdf.save()

def draw_image(pdf, image_path, x, y):
    # Ouverture de l'image pour obtenir ses dimensions
    image = Image.open(image_path)
    width, height = calculate_dimensions(image)
    # Ajout de l'image au canvas PDF
    pdf.drawImage(image_path, x, y, width=width, height=height)

def calculate_dimensions(image):
    # Calcul des dimensions pour que l'image rentre dans la page tout en préservant ses proportions
    largeur, hauteur = image.size
    rapport_aspect = largeur / float(hauteur)

    if rapport_aspect > 1:
        width = pyautogui.size()[1]
        height = pyautogui.size()[1] / rapport_aspect
    else:
        width = pyautogui.size()[1] * rapport_aspect
        height = pyautogui.size()[1]

    return width, height

def calculate_height(image_path):
    # Calcul de la hauteur pour l'emplacement de la deuxième image
    return calculate_dimensions(Image.open(image_path))[1]

def main():
    url_du_site = "https://Votre.site.com" #À MODIFIER, entrez l'url du site désiré
    nom_du_screenshot = "screenshot_page_{}.png"
    nombre_max_screenshots = 100 #100 par défault, peut être augmenté
    output_pdf = 'output.pdf'#output.pdf par défault, peut etre modifié

    prendre_screenshot(url_du_site, nom_du_screenshot, nombre_max_screenshots, output_pdf)

if __name__ == "__main__":
    main()