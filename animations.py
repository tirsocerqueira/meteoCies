from datetime import datetime
import tweepy
import urllib.request
import os
from PIL import Image
import subprocess

# API Values
api_key = 'sx2k9Hf6CGrqeiAGkTSF2N5fG'
api_secret = '2rdovbtb3m4Gwd2aZlwdfWtkfOrZLYzjzXFYIj6VLoTVQDJ136'
access_token = '1619107870234054656-LYlIPmGVTUpTo5Oqsb6kBYQrZHdNwz'
access_token_secret = 'wdE57hblXOumLXD5UUsDflHewqUgQFetxB5tBgLfwlduI'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAP57ogEAAAAAMvsnLe8L36qsN1cpDdfGuKiYv0w%3DesKHhH238WEUBWniDBOHyzGaUJbFliH5q78Uz8BatsoBqbeyOi'

def round_to_quarter_hour(minute):
    """
    Redondea el minuto proporcionado al minuto más cercano en el cuarto de hora correspondiente.
    """
    if minute < 8:
        return 0
    elif minute < 23:
        return 15
    elif minute < 38:
        return 30
    elif minute < 53:
        return 45
    else:
        return 0

def nearest_quarter_minute(hour, minute):
    """
    Calcula el minuto más cercano a cada cuarto de la hora para la hora dada.
    """
    quarter_hour = round_to_quarter_hour(minute)
    if quarter_hour == 0:
        hour = (hour + 1) % 24
    return hour, quarter_hour


# Set local day
now = datetime.now()
minutos = [0,15,30,45]
# URL changes depending on the day, month and year
# It must be changed the str(20)
nearest_hour, nearest_minute = nearest_quarter_minute(now.hour-1,now.minute)
starting_hour = nearest_hour-4
hour=starting_hour
minute= nearest_minute
for hour in range(hour,nearest_hour):
    for minute in minutos:
        url = "https://www.meteogalicia.gal/datosred/satelite/ULTIMOS_30_DIAS/IMAGENES/Monthly/Day%"+ str(20)+now.strftime('%d') +"/WEB_HRVIBERIA_"+"["+ "{:02d}".format(hour) +"-" + "{:02d}".format(minute) +"]"+".jpg"
        #VIDEO FILE FOR LAST HOUR NUBOSITY
        # Download of the file
        print(hour,minute)
        name=str(now.day)+str(now.month)+str(now.year)+"lastHour"+"{:02d}".format(hour) + "{:02d}".format(minute) + ".jpg"
        try:
            print("Downloading starts...\n")
            urllib.request.urlretrieve(url, name)
            # abrir la imagen
            imagen = Image.open(name)

            # establecer el centro de zoom
            centro_x = 550
            centro_y = 350

            # establecer el factor de zoom
            factor_zoom = 3

            # obtener el tamaño original de la imagen
            ancho_original, alto_original = imagen.size

            # calcular el tamaño del extracto de la imagen
            ancho_extracto = int(ancho_original / factor_zoom)
            alto_extracto = int(alto_original / factor_zoom)

            # calcular la posición de la esquina superior izquierda del extracto
            x1 = centro_x - ancho_extracto // 2
            y1 = centro_y - alto_extracto // 2

            # calcular la posición de la esquina inferior derecha del extracto
            x2 = x1 + ancho_extracto
            y2 = y1 + alto_extracto

            # recortar el extracto de la imagen
            imagen_extracto = imagen.crop((x1, y1, x2, y2))

            # guardar el extracto de la imagen
            imagen_extracto.save(name)
            print("Download completed..!!")
        except Exception as e:
            print(e)



# Directorio donde se encuentran las imágenes
directorio_imagenes = '/Users/tirsocerqueira/PycharmProjects/pythonProject'

# Ruta y nombre del archivo de video que se generará
ruta_archivo_video = 'last2hours_nubosity.mp4'

# Definir los parámetros del archivo de video
fps = 1
altura = 720
ancho = 1280

# Lista de archivos en el directorio
lista_archivos = os.listdir(directorio_imagenes)

# Ordenar la lista por fecha de creación
lista_archivos.sort(key=lambda x: os.path.getctime(os.path.join(directorio_imagenes, x)))

# Lista de imágenes
lista_imagenes = []

# Recorrer la lista de archivos y agregar las imágenes a la lista de imágenes
for archivo in lista_archivos:
    if archivo.endswith('.jpg'):
        ruta_archivo = os.path.join(directorio_imagenes, archivo)
        imagen = Image.open(ruta_archivo)
        imagen = imagen.resize((ancho, altura))
        lista_imagenes.append(imagen)

# Crear el archivo de video con FFmpeg
cmd = f"ffmpeg -y -f image2pipe -r {fps} -s {ancho}x{altura} -i - -vcodec libx264 -pix_fmt yuv420p -r {fps} {ruta_archivo_video}"
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, shell=True)


# Agregar cada imagen al archivo de video
for imagen in lista_imagenes:
    imagen.save(p.stdin, 'JPEG')

# Cerrar el proceso FFmpeg
p.stdin.close()
p.wait()

name ="last2hours_nubosity.mp4"

# Authenticating
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
# Create API object
api = tweepy.API(auth)
# Uploading the video
path="/Users/tirsocerqueira/PycharmProjects/pythonProject/"+ name
upload_result = api.media_upload(path, media_category="tweet_video")

#OJO QUE HAY QUE CAMBIAR LA
api.update_status(status= "|| " + str(now.hour)+":"+str(now.minute)+ " || Evolución de las nubes en las últimas 2 horas " + str(now.day) + "/" + str(now.month)+"/" + str(now.year) , media_ids=[upload_result.media_id_string])
