# MIME > Multipupose Internet Mail Extensions
from email.mime.multipart import MIMEMultipart  # Para crear el mensaje
from email.mime.text import MIMEText  # Para crear el contenido del mensaje
# SMTP > Simple Mail Transfer Protocol
from smtplib import SMTP  # Para enviar el mensaje
from validate_email import validate_email
from os import environ

def cambiarPassword(destinatario):
    existeEmail = validate_email(destinatario)

    if not existeEmail:
        print("El correo no existe")
        return

    texto ='''Hola
    Parece que has cambiado tu contraseña, si no fuiste tú comunicate con nosotros, caso contrario, ignora este mensaje'''
    emailEmisor = environ.get('CORREO_EMISOR')#'goldengpa23@gmail.com'
    passwordEmisor = environ.get('PASSWORD_CORREO_EMISOR')#'msqkbfzrfciratdk'

    cuerpo = MIMEText(texto, 'plain') # texto plano > 
    correo = MIMEMultipart() # para poder adjuntar el cuerpo del correo y configurar el correo 

    # configuramos el titulo del correo
    correo['Subject'] = 'Cambiaste tu contraseña'

    # configuramos el destinatario del correo
    correo['To'] = destinatario

    # acá adjuntamos el cuerpo del correo
    correo.attach(cuerpo)
    
    #                   SERVIDOR      | PUERTO
    # outlook > outlook.office365.com | 587
    # hotmail > smtp.live.com         | 587
    # gmail >   smtp.gmail.com        | 587
    # icloud >  smtp.mail.me.com      | 587
    # yahoo >   smtp.mail.yahoo.com   | 587
    emisor = SMTP('smtp.gmail.com',587)
    emisor.starttls()

    # inicio sesion con mis credenciales
    emisor.login(emailEmisor, passwordEmisor)

    # enviamos el correo
    emisor.sendmail(from_addr=emailEmisor, to_addrs=destinatario, msg=correo.as_string())

    emisor.quit()

    print("Correo enviado exitosamente")