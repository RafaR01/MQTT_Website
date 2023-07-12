from flask import Flask
import paho.mqtt.client as mqtt
import os

app = Flask(__name__)
mqtt_broker = "192.168.138.237"  # Replace with your MQTT broker's URL
mqtt_topic = "control_topic"  # Topic to publish when the value is 1
mqtt_username = "rafael"  # MQTT broker username
mqtt_password = "rafael"  # MQTT broker password

@app.route('/button')
def button():
    # Toggle the value
    value = read_value()
    if value == "start":
        value = "stop"
        publish_mqtt(value)
    else:
        value = "start"
        publish_mqtt(value)

    # Write the updated value to the file
    write_value(value)

    return 'Button clicked'

def read_value():
    with open('value.txt', 'r') as file:
        return file.read().strip()

def write_value(value):
    with open('value.txt', 'w') as file:
        file.write(value)

def publish_mqtt(value):
    client = mqtt.Client()
    client.username_pw_set(username=mqtt_username, password=mqtt_password)
    client.connect(mqtt_broker)
    client.publish(mqtt_topic, value)

if __name__ == '__main__':
    app.run()
