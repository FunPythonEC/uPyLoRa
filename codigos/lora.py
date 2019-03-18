from time import sleep
import config_lora
from sx127x import SX127x
from controller_esp32 import ESP32Controller
import _thread
class LoRa:

	#Iniciamos el objeto de lora de acuerdo a los pines establecidos para las placas
	#TTGO y Heltec con el chip sx127x
	def __init__(self, header=None, period=0):
		#Se especifica la cabecera en caso de que solo se quiera procesar algo en especifico
		#y tambien un periodo por si se quiere hacer cierta accion de manera periodica

		self.header = header
		self.period = float(period)
		self.status = 1
		self.cb = None

		self.controller = ESP32Controller()
		self.lora = self.controller.add_transceiver(SX127x(name = 'LoRa'),
								pin_id_ss = ESP32Controller.PIN_ID_FOR_LORA_SS,
								pin_id_RxDone = ESP32Controller.PIN_ID_FOR_LORA_DIO0)


	def __del__(self):
		print("LoRa object deleted")

	def stop(self):
		self.status = 0

	def go_on(self):
		self.status = 1

	#permite enviar un dato con el header especificado en la construccion del objeto
	#o con un header distinto
	def send(self, data, spheader=None):
		if spheader is not None:
			self.lora.println(str(spheader)+'@'+str(data))
		elif self.header is not None:
			self.lora.println(str(self.header)+'@'+str(data))
		else:
			self.lora.println(str(data))

	#metodo para escuchar algun mensaje y ejecutar el callback
	def wait_msg(self):
		assert self.cb is not None, "Subscribe callback is not set"
		def inc_msg():
			while 1:
				if self.status:
					if self.lora.receivedPacket():
						try:
							payload = self.lora.read_payload().decode()
							data = payload.split('@')
							if len(data)==2:
								if self.header is not None:
									payload = payload.split('@')
									if payload[0] == str(self.header):
										self.cb(payload[1])
								else:
									pass
							elif self.header is None:
								self.cb(payload)
							sleep(self.period)
						except Exception as e:
							print(e)
		_thread.start_new_thread(inc_msg, ())
		

	def set_callback(self, f):
		self.cb = f

	#metodo para el recibimiento de paquetes
	def receive_msg(self):
		assert self.cb is not None, "Subscribe callback is not set"
		if self.lora.receivedPacket():
			try:
				payload = self.lora.read_payload().decode()
				data = payload.split('@')
				if len(data)==2:
					if self.header is not None:
						payload = payload.split('@')
						if payload[0] == str(self.header):
							self.cb(payload[1])
					else:
						pass
				elif self.header is None:
					self.cb(payload)
			except Exception as e:
				print(e)
