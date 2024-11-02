# sudo apt install mosquitto mosquitto-clients
# sudo systemctl start mosquitto
# sudo ufw disable
# sudo ufw allow 1883
#pip3 install paho-mqtt
import paho.mqtt.client as mqtt
import subprocess
import os
import time
import cv2 as cv #sudo apt install python3-opencv

def rotate_to_target(start_angle, end_angle):

    # Call the Bash script with the numbers as arguments
    result = subprocess.run(
        ['bash', 'motor/run.sh', str(start_angle), str(end_angle)],  # Pass the numbers as strings
        check=True,
        capture_output=True,
        text=True
    )

# need to run from the /person_alarm_project/
def execute_person_detection():
        
    result = subprocess.run(['bash', 'docker_tf_lite/run.sh'], check=True, capture_output=True, text=True)
    print(f"{result.stdout}")

    if os.path.isfile('/home/liran/person_alarm/docker_tf_lite/person.jpeg'):
        return 'person detected'
    else:
        return 'no alarm'


# Define the callback for when a message is received
def on_message(client, userdata, msg):
    
    print(f"Received message: {msg.payload.decode()}")    

    print('rotate to alarm')
    rotate_to_target(0, 180)
    print('finised rotate ....')

    print('capture ....')

    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit(-1)
    time.sleep(1)
    ret, frame = cap.read()    
    cv.imwrite('/home/liran/person_alarm/docker_tf_lite/alarm.jpeg',frame)  
    cap.release()
    
    print('rotate back to default tocation ')
    rotate_to_target(180, 0)


    print('checking if thre is a person ,,,')
    response = execute_person_detection()
    print(f'{response}')

    client.publish("response/topic", response)

    exit(0)

# Create a client instance
client = mqtt.Client(callback_api_version=1)
client.on_message = on_message

# Connect to the broker
client.connect("192.168.43.110", 1883, 60)

# Subscribe to a topic
client.subscribe("request/topic")

# Start the loop
client.loop_forever()


