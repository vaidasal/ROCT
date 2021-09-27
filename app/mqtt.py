import paho.mqtt.client as mqtt

TOPIC = "roct/json/vaidas"
BROKER_ADDRESS = "53.188.69.136"
PORT = 1883
QOS = 0

class Mqtt:

    #TOPIC = "roct/json/vaidastest"
    TOPIC = "DAI/MBP/E/XBO/JSON/0/GENERIC/0500/TestRoctBa40/LAM/ROCT/MEASURE/V1"
    TOPICUSER = "DAI/MBP/E/XBO/JSON/0/INTEGRAGW/0500/TestRoctBa40/LAM/ROCT/USER/V1"
    BROKER_ADDRESS = "msb-dev.de050.corpintra.net"
    # BROKER_ADDRESS = "53.188.69.136"
    PORT = 1883
    QOS = 2
    client = mqtt.Client()

    def sendMessage(self, message):

        self.client.connect(self.BROKER_ADDRESS, PORT)

        print("Connected to MQTT Broker: " + self.BROKER_ADDRESS)

        DATA = message

        self.client.publish(self.TOPIC, DATA, qos=QOS)

        self.client.loop()

    def sendUser(self, message):

        self.client.connect(self.BROKER_ADDRESS, PORT)

        print("Connected to MQTT Broker: " + self.BROKER_ADDRESS)

        DATA = message

        self.client.publish(self.TOPICUSER, DATA, qos=QOS)

        self.client.loop()