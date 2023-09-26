import requests
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
from dataBase import readData
from milirocket import display_milirocket_vte
import os
import threading

# Poner aquí todo lo de envio de datos a la paguina
def fire_base():
    while True:
        data = readData()
        cambio = data[1]
        velocidad = data[2]
        distancia = data[3]

# Configuración inicial del display OLED
RST = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height

# Carpeta donde se guardarán las fuentes descargadas desde Google Fonts
fonts_folder = "fonts"

# Verifica si la carpeta de fuentes existe, si no, créala
if not os.path.exists(fonts_folder):
    os.makedirs(fonts_folder)

# URLs de las fuentes desde Google Fonts y descarga
fonts = {
    "opensans": "https://fonts.gstatic.com/s/opensans/v18/mem8YaGs126MiZpBA-UFVZ0e.ttf",
}

for font_name, font_url in fonts.items():
    font_filename = os.path.join(fonts_folder, f"{font_name}.ttf")
    response = requests.get(font_url)
    with open(font_filename, "wb") as font_file:
        font_file.write(response.content)

# Carga las fuentes descargadas desde la carpeta
font1 = ImageFont.truetype(os.path.join(fonts_folder, "opensans.ttf"), 20)
font2 = ImageFont.truetype(os.path.join(fonts_folder, "opensans.ttf"), 10)

# Creación de una imagen en blanco para el display OLED
image1 = Image.new('1', (width, height))
draw = ImageDraw.Draw(image1)
draw.rectangle((0, 0, width, height), outline=0, fill=0)
background_color = 0

display_milirocket_vte()

# Configuración de la plantilla de texto en la imagen
draw.rectangle((0, 0, width, height), outline=0, fill=0)
disp.clear()
disp.display()
draw.text((0, -2), "Cambio:", font=font1, fill=255)
draw.text((0, 29), "Vel:", font=font2, fill=255)
draw.text((0, 50), "Dist:", font=font2, fill=255)

# Crear y arrancar el hilo para imprimir los valores
print_thread = threading.Thread(target=fire_base)
print_thread.daemon = True  # Hace que el hilo se detenga cuando el programa principal se detenga
print_thread.start()

# Bucle principal para actualizar el contenido en el display OLED
while True:
    data = readData()
    cambio = data[1]
    velocidad = data[2]
    distancia = data[3]

    # Borra los valores anteriores
    draw.rectangle([(100, -2), (120, 25)], fill=background_color)
    draw.rectangle([(25, 21), (94, 49)], fill=background_color)
    draw.rectangle([(30, 50), (114, 63)], fill=background_color)
    
    # Dibuja los nuevos valores
    draw.text((100, -2), str(cambio), font=font1, fill=255)
    draw.text((25, 18), str(velocidad), font=font1, fill=255)
    draw.text((95, 29), "Km/H", font=font2, fill=255)
    draw.text((30, 50), str(distancia), font=font2, fill=255)
    draw.text((115, 50), "m", font=font2, fill=255)

    # Actualiza el display OLED con la imagen
    disp.image(image1)
    disp.display()