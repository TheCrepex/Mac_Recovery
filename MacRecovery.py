# Python 3 code to print MAC
# in formatted way.



# joins elements of getnode() after each 2 digits.


import uuid
import paho.mqtt.client as mqtt
import time

# Definir la dirección del servidor MQTT
broker_address = "172.30.2.114"  # Cambia a la dirección IP de tu servidor

# Definir el puerto del servidor MQTT (generalmente es 1883)
broker_port = 1883

# Definir el nombre del tema al que enviarás los datos
topic = "mac_topic"

# Crear un cliente MQTT
client = mqtt.Client()

# Conectar al servidor MQTT
client.connect(broker_address, broker_port, 60)

try:
    while True:
        # Simular la obtención de la dirección MAC (puedes reemplazar esto con tu lógica)
        MAC =(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
        for ele in range(0,8*6,8)][::-1]))
        print (MAC)

        # Publicar la dirección MAC en el tema especificado
        client.publish(topic, MAC)

        # Esperar antes de enviar el siguiente mensaje (ajusta según tus necesidades)
        time.sleep(5)

except KeyboardInterrupt:
    # Desconectar el cliente MQTT al salir
    client.disconnect()
