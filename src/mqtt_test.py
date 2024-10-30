# sudo apt install mosquitto mosquitto-clients
# sudo systemctl start mosquitto
# sudo ufw disable
# sudo ufw allow 1883
#pip3 install paho-mqtt
import paho.mqtt.client as mqtt

# Define the callback for when a message is received
def on_message(client, userdata, msg):
    
    print(f"Received message: {msg.payload.decode()}")
    # Send a response
    response = "Hello from pi 5!"
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
