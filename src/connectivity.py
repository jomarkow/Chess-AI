import paho.mqtt.client as mqtt

from config.config import *

class Broker:
    
    def __init__(self):
        
        self.client = mqtt.Client()
        
        try:
            self.client.connect(ADDRESS, PORT)
        except:
            raise ConnectionError("Could not connect to MQTT broker")
        
    def send_data(self, topic, message):
        
        self.client.publish(topic, message)
        
    def check_ack(self):
        
        def on_message(client, userdata, message):
            
            print(f"Received message on topic '{message.topic}': {message.payload.decode()}")
            client.loop_stop()
        
        self.client.on_message = on_message
        self.client.loop_start()
        self.client.loop_forever()
        
    def disconnect(self):
        
        self.client.disconnect