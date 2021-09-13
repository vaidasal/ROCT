import paho.mqtt.client as mqtt

TOPIC = "roct/json/vaidas"
BROKER_ADDRESS = "53.188.69.136"
PORT = 1883
QOS = 0

class Mqtt:

    TOPIC = "roct/json/vaidastest"
    #TOPIC = "DAI/MBP/E/XBO/JSON/0/INTEGRAGW/0500/TestRoctBa40/LAM/ROCT/MEASURE/V1"
    BROKER_ADDRESS = "53.188.69.136"
    #BROKER_ADDRESS = "msb-dev.de050.corpintra.net"
    PORT = 1883
    QOS = 2
    client = mqtt.Client()

    def sendMessage(self, message):

        self.client.connect(BROKER_ADDRESS, PORT)

        print("Connected to MQTT Broker: " + BROKER_ADDRESS)

        DATA = message

        self.client.publish(TOPIC, DATA, qos=QOS)

        self.client.loop()