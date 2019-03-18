Estos códigos han sido recopilados de otro repositorio con el fin de mejorar su uso, para que el único script que se maneje como librería sea lora.py, será mejorado con el tiempo.
Referencia: https://github.com/lemariva/uPyLora

En el repositorio se puede encontrar:

* códigos: contiene todos los scripts utilizados para dar uso del chip sx1276

  * config_lora.py

  * controller.py

  * controller_esp32.py

  * esp32lora.bin

  * sx127x.py

  * lora.py

    De los cuales en el que nos concentramos es el de lora.py el cual tiene la clase con sus métodos, facilitando el uso del chip. Para este caso se ha especificado que la frecuencia usada es de 915 MHz, configurado en el archivo `sx127x.py`, en caso de que se desee una frecuencia distinta es necesario que sea cambiado en el script y luego volver ha formar el .bin o tan solo ingresar los scripts necesarios en el ESP.

* ejemplos: contiene ejemplos sobre como debe ser usada la clase, para enviar y recibir datos, además de la subida de datos a un servicio web como el de ubidots.

# lora.py

Principalmente este archivo, se ha creado para instanciar un objeto especificado como LoRa, el cual tendra todos los metodos necesarios para enviar y recibir código. Los pines que se usan para la comunicación con el chip de LoRa son los mismo especificados en la documentación de HelTec y TTGO los cuales hacen placas de desarrollo con el microcontrolador ESP32 agregandole un chip sx127x con antena. A continuación se encontrará como usar la librería con sus métodos:

## Construcción de clase LoRa

El script contiene a LoRa el cual es una clase para poder inicializar el uso del chip sx127x. Se puede inicializar de la siguiente manera:

~~~~ python
from lora import LoRa

lora = LoRa()

#si se desea un filtrado de los mensajes
lora = LoRa(header='header')
~~~~

Además para la recepción de datos periódicas la cual se maneja con el metodo de wait_msg(), se puede especificar un periodo, para que despues de haber llegado un mensaje, especificar cuanto tiempo se quiere que pase hasta recibir uno nuevo, de la siguiente manera:


~~~~ python
#sin header
lora = LoRa(period=2)

#con header
lora= LoRa(header='header',period=2)
~~~~

## Metodos

### send('mensaje', spheader = 'headerespecifico')

Es el método especificado para enviar datos, de manera que el primer parametro es para especificar que dato se quiere enviar y el segundo en caso que se quiera mandar con un header específico.
~~~~ python
#sin header especifico
lora.send('hola')

#con header especifico
lora.send('hola', spheader = 'headersp')
~~~~
La variables de un header especifico ha sido agregado en caso de que en algún momento se necesite enviar un mensaje con un header distinto o especifico.

### set_callback(cb)

Al igual que un objeto de mqtt para un subscribe, utilizamos el mismo concepto para callbacks, de manera que una vez instanciado el objeto de lora, se especifica que funcion se quiere que se ejecute cuando llegue un mensaje:

~~~~ python
#cb corresponde al nombre de la funcion usada como callback
#que debe tener como parametro una variable que sera el mensaje
lora.set_callback(cb)
~~~~

### wait_msg()
~~~~ python
lora.wait_msg()
~~~~
Una vez que ya esta especificado nuestro callback, wait_msg se encarga para que en segundo plano se escuche los mensajes entrantes y que nuestro callback se ejecute. En el caso de que en al instanciar la clase LoRa, se especifique un valor para la variable period, una vez que se recibe un mensaje, tendra que pasar el tiempo (en segundos) especificado para que otro mensaje sea aceptado.

### receive_msg()
~~~~ python
lora.receive_msg()
~~~~
Parecido a wait_msg() se encarga de recibir un mensaje en un momento especifico, por una sola vez y se ejecuta el callback cuando llegue el mensaje.


# Licencia

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">uPyLoRa</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/FunPythonEC/LibreriasDesarrolladas/tree/master/uPyLoRa" property="cc:attributionName" rel="cc:attributionURL">Steven Silva</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Reconocimiento-CompartirIgual 4.0 Internacional License</a>.<br />Creado a partir de la obra en <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/lemariva/uPyLora" rel="dct:source">https://github.com/lemariva/uPyLora</a>.
