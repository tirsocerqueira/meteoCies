import requests

# Cangas => 10906
# Cies Alto => 10125
# Puerto Vigo => 14001
# Cies Boya => 15002

# URL Data for buoyancy
url_boya = "https://servizos.meteogalicia.gal/mgrss/observacion/ultimos10minPlataformas.action?idEst=15002"

# Data extraction from buoyancies
data = requests.get(url_boya).json()
estacion = data['listUltimos10min'][0]['estacion']
viento = data['listUltimos10min'][0]['listaMedidas'][7]['valor']
dir_viento = data['listUltimos10min'][0]['listaMedidas'][3]['valor']
racha = data['listUltimos10min'][0]['listaMedidas'][4]['valor']
dir_racha = data['listUltimos10min'][0]['listaMedidas'][2]['valor']
temperatura = data['listUltimos10min'][0]['listaMedidas'][6]['valor']
# Data convertion m/s to kn
viento = viento * 1.94384
racha = racha * 1.94384

#Tweet format
tweet = "Cies" + "\n" + "Wind: " + str(round(viento, 2)) + "\n" + "Dir: " + str(dir_viento) + "\n" + "Shift: " + str(round(racha,2)) + "\n" + "Shift-dir: " + str(dir_racha) + "\n" + "Tª agua: " + str(round(temperatura,2)) +"\n\n"

# Data extraction from static stations
# First station
url_estaciones = "https://servizos.meteogalicia.gal/mgrss/observacion/ultimos10minEstacionsMeteo.action?idParam=VV_AVG_10m,VV_RACHA_10m,DV_AVG_10m,DV_CONDICION_10m&idEst=10906"
data = requests.get(url_estaciones).json()
estacion = data['listUltimos10min'][0]['estacion']
viento = data['listUltimos10min'][0]['listaMedidas'][2]['valor']
dir_viento = data['listUltimos10min'][0]['listaMedidas'][0]['valor']
racha = data['listUltimos10min'][0]['listaMedidas'][3]['valor']
dir_racha = data['listUltimos10min'][0]['listaMedidas'][1]['valor']
# Data convertion m/s to kn
viento = viento * 1.94384
racha = racha * 1.94384
tweet = tweet + estacion + "\n" + "Wind: " + str(round(viento, 2)) + "\n" + "Dir: " + str(
    dir_viento) + "\n" + "Shift: " + str(round(racha, 2)) + "\n" + "Shift-dir: " + str(
    dir_racha) + "\n\n"

# Second station
url_estaciones = "https://servizos.meteogalicia.gal/mgrss/observacion/ultimos10minEstacionsMeteo.action?idParam=VV_AVG_10m,VV_RACHA_10m,DV_AVG_10m,DV_CONDICION_10m&idEst=10125"
data = requests.get(url_estaciones).json()
estacion = data['listUltimos10min'][0]['estacion']
viento = data['listUltimos10min'][0]['listaMedidas'][3]['valor']
dir_viento = data['listUltimos10min'][0]['listaMedidas'][1]['valor']
racha = data['listUltimos10min'][0]['listaMedidas'][2]['valor']
dir_racha = data['listUltimos10min'][0]['listaMedidas'][0]['valor']
# Data convertion m/s to kn
viento = viento * 1.94384
racha = racha * 1.94384
tweet = tweet + estacion + "\n" + "Wind: " + str(round(viento, 2)) + "\n" + "Dir: " + str(
    dir_viento) + "\n" + "Shift: " + str(round(racha, 2)) + "\n" + "Shift-dir: " + str(
    dir_racha) + "\n\n"


# Third station
url_estaciones = "https://servizos.meteogalicia.gal/mgrss/observacion/ultimos10minEstacionsMeteo.action?idParam=VV_AVG_10m,VV_RACHA_10m,DV_AVG_10m,DV_CONDICION_10m&idEst=14001"
data = requests.get(url_estaciones).json()
estacion = data['listUltimos10min'][0]['estacion']
viento = data['listUltimos10min'][0]['listaMedidas'][2]['valor']
dir_viento = data['listUltimos10min'][0]['listaMedidas'][0]['valor']
racha = data['listUltimos10min'][0]['listaMedidas'][3]['valor']
dir_racha = data['listUltimos10min'][0]['listaMedidas'][1]['valor']
# Data convertion m/s to kn
viento = viento * 1.94384
racha = racha * 1.94384
tweet = tweet + estacion + "\n" + "Wind: " + str(round(viento, 2)) + "\n" + "Dir: " + str(
    dir_viento) + "\n" + "Shift: " + str(round(racha, 2)) + "\n" + "Shift-dir: " + str(
    dir_racha) + "\n\n"

# Graphic data
# Buoyancy station
# url_graph_wind_boya="http://www2.meteogalicia.gal/galego/observacion/plataformas/graficasactuais/ventoracha_h015002.jpg"
# url_graph_direction_boya="http://www2.meteogalicia.gal/galego/observacion/plataformas/graficasactuais/dirventoracha_h015002.jpg"


print (tweet)