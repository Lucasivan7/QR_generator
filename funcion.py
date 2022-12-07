# Importamos la libreria para generar el codigo QR
import qrcode
from PIL import Image
from datetime import date, datetime
from datetime import timedelta

# Pasamos el logo que vamos a utilizar en el qr code como una imagen
logo_link = '/Users/lucascaballero/Desktop/Prueba_Qr/static/logo.jpg'
logo = Image.open(logo_link)

    # Pasamos los parametros de tamaño y color para nuestro codigo QR
basewidth = 100
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

# Creamos una variable para almacenar el codigo de error en caso de que al generar el QR ocurra un errors
Qrcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)


primer_dia = "2022-11-20"
primer_dia = datetime.strptime(primer_dia, "%Y-%m-%d")
hoy = datetime.now()
dia_de_bootcamp = hoy - primer_dia

def actu_url(url_base, dia_bootcamp): 
    url_nueva = url_base + str(dia_bootcamp)
    return url_nueva



url_dia = actu_url("check-in/", str(dia_de_bootcamp.days))


# Generamos la ruta a la que nuestro codigo QR va a redireccionar
url = 'http://192.168.3.16:5500/' + url_dia
Qrcode.add_data(url)
# Generamos el codigo QR
qrcode.make()

# Pasamos los parametros de color y posicion de nuestro logo, tambien definimos el color que tendra nuestro QR
qrcolor = 'Black'
qrimg = Qrcode.make_image(fill_color=qrcolor, back_color="white").convert('RGB')
pos = ((qrimg.size[0] - logo.size[0]) // 2, (qrimg.size[1] - logo.size[1]) // 2)
qrimg.paste(logo, pos)
# Guardamos nuestro codigo QR generado como una imagen
qrimg.save('qr_penguin.png')
# Mostramos un texto una vez que el codigo QR haya sido generado con exito
print('Codigo QR generado con exito')