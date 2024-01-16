import subprocess
import uuid
import paho.mqtt.client as mqtt
import time

def get_mac_address():
    try:
        result = subprocess.check_output(["ifconfig", "eth0"]).decode("utf-8")
        if "HWaddr" in result:
            mac_address = result.split("HWaddr")[1].split("\n")[0].strip()
            return mac_address
        else:
            return "No se pudo obtener la dirección MAC"
    except Exception as e:
        print(f"Error al obtener la dirección MAC: {e}")
        return None

# Definir la dirección del servidor MQTT
broker_address = "172.30.2.135"  # Cambia a la dirección IP de tu servidor

# Definir el puerto del servidor MQTT (generalmente es 1883)
broker_port = 1884

# Definir el nombre del tema al que enviarás los datos
topic = "mac_address_topic"


# Crear un cliente MQTT
client = mqtt.Client()

# Conectar al servidor MQTT
client.connect(broker_address, broker_port, 60)
while True:
    try:

            # Simular la obtención de la dirección MAC (puedes reemplazar esto con tu lógica)
        MAC =(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))
        print (MAC)

            # Publicar la dirección MAC en el tema especificado
        client.publish(topic, MAC)

            # Esperar antes de enviar el siguiente mensaje (ajusta según tus necesidades)
        client.disconnect()
        break

    except KeyboardInterrupt:
        # Desconectar el cliente MQTT al salir
        client.disconnect()
