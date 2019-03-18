from lora import LoRa

#se inicializa el objeto de lora sin header
lora = LoRa()

#en el caso de que se desee un header para el filtrado de los mensajes
#lorawhead = LoRa(header = 'header')
#de manera los mensajes llevaran ese header para ser filtrados de otros

#send(msg) envia msg a traves del chip de lora
msg = 'hola desde tierra'
lora.send(msg)