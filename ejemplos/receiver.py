import lora

#funcion de callback necesaria para manejar mensajes de entrada
def cb(msg):
    print(msg)

#se inicializa el objeto de lora sin header
lora = LoRa()

#en el caso de que se desee un header para el filtrado de los mensajes
#lorawhead = LoRa(header = 'header')
#de manera que asi solo los mensajes que tengan esa cabecera seran recibidos

lora.set_callback(cb) #se especifica que funcion funcionara de callback
lora.wait_msg() #se dispone a escuchar mensajes entrantes en segundo plano

#para el recibimiento de un mensaje en un momento especifico usar
#lora.receive_msg()

