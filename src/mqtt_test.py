# sudo apt install mosquitto mosquitto-clients
# sudo systemctl start mosquitto
# sudo ufw disable
# sudo ufw allow 1883
#pip3 install paho-mqtt
import paho.mqtt.client as mqtt
import subprocess
import os


def rotate_to_target():
    return

# need to run from the /person_alarm_project/
def execute_person_detection():
        
    result = subprocess.run(['bash', 'docker_tf_lite/run.sh'], check=True, capture_output=True, text=True)
    print(f"{result.stdout}")

    if os.path.isfile('docker_tf_lite/person.jpeg'):
        print('person detected !!!!')
        return True
    else:
        print('no alarm ')  
        return False

execute_person_detection()

# Define the callback for when a message is received
def on_message(client, userdata, msg):
    
    print(f"Received message: {msg.payload.decode()}")    

    rotate_to_target()

    response = "no alarm"
    if execute_person_detection():
        response = "person detected "

    client.publish("response/topic", response)

# Create a client instance
client = mqtt.Client(callback_api_version=1)
client.on_message = on_message

# Connect to the broker
client.connect("192.168.43.110", 1883, 60)

# Subscribe to a topic
client.subscribe("request/topic")

# Start the loop
client.loop_forever()


