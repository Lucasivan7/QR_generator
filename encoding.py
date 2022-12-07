# Importamos la libre de json web token, que nos servira para encriptar la url.
import jwt

# Realizamos la encriptacion de la url
encoded_jwt = jwt.encode({'some': 'http://192.168.3.16:5500 this is a test.html'}, 'secret', algorithm='HS256')
print(encoded_jwt)