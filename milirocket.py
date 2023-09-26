import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
from time import sleep
import os

def display_milirocket_vte():
    # Configuración del display OLED
    RST = 0
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
    disp.begin()
    disp.clear()
    disp.display()
    width = disp.width
    height = disp.height

    # Creación de una imagen en blanco para el display OLED
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Carpeta donde se guardarán las fuentes descargadas desde Google Fonts
    fonts_folder = "fonts"

    # Configuración de la fuente
    font = ImageFont.truetype(os.path.join(fonts_folder, "opensans.ttf"), 25)

    # Muestra "MiliRocket" en la primera línea
    draw.text((0, 0), "MiliRocket", font=font, fill=255)

    # Salto de línea
    draw.text((0, 16), "\n", font=font, fill=255)

    # Muestra "VTE" en la segunda línea
    draw.text((38, 25), "VTE", font=font, fill=255)

    # Actualiza el display OLED con la imagen
    disp.image(image)
    disp.display()
    sleep(3)

if __name__ == "__main__":
    display_milirocket_vte()