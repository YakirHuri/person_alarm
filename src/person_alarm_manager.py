# sudo apt install mosquitto mosquitto-clients
# sudo systemctl start mosquitto
# sudo ufw disable
# sudo ufw allow 1883
# sudo apt install python3-paho-mqtt

import paho.mqtt.client as mqtt
import subprocess
import os
import time
import cv2 as cv #sudo apt install python3-opencv

def rotate_to_target(start_angle_x, end_angle_x, start_angle_y, end_angle_y):

    # of the x 
    result = subprocess.run(
        ['bash', 'motor/run.sh', str(start_angle_x), str(end_angle_x),  str(11)],  # Pass the numbers as strings
        check=True,
        capture_output=True,
        text=True
    )
    time.sleep(2)
    # # for y
    result = subprocess.run(
        ['bash', 'motor/run.sh', str(start_angle_y), str(end_angle_y), str(13)],  # Pass the numbers as strings
        check=True,
        capture_output=True,
        text=True
    )

#
# this is the center command !!!
rotate_to_target(0, 180, 0, 125 ) 

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

    msg =   msg.payload.decode()
    if msg  == "left": 
        rotate_to_target(180, 270, 115,0 ) #left
        print('rotate to alarm')
        print('finised rotate ....')

        print('capture ....')

        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit(-1)
        time.sleep(5)
        ret, frame = cap.read()    
        cv.imwrite('/home/liran/person_alarm/docker_tf_lite/alarm.jpeg',frame)  
        cap.release()
        time.sleep(2)
        print('rotate back to default tocation ')
        rotate_to_target(0, 180, 0, 130  ) 


        

        print('checking if thre is a person ,,,')
        response = execute_person_detection()
        print(f'the response is {response}')

        client.publish("response/topic", response)
    elif msg == 'right':
        rotate_to_target(180, 30, 115,20  ) # right  
        print('rotate to alarm')
        print('finised rotate ....')

        print('capture ....')

        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit(-1)
        time.sleep(5)
        ret, frame = cap.read()    
        cv.imwrite('/home/liran/person_alarm/docker_tf_lite/alarm.jpeg',frame)  
        cap.release()
        time.sleep(2)
        print('rotate back to default tocation ')
        rotate_to_target(0, 212, 0, 125  ) 


        

        print('checking if thre is a person ,,,')
        response = execute_person_detection()
        print(f'the response is {response}')

        client.publish("response/topic", response)
    


    
    
# Create a client instance
client = mqtt.Client(callback_api_version=1)
client.on_message = on_message
# Connect to the broker
client.connect("192.168.43.253", 1883, 60)

# Subscribe to a topic
client.subscribe("request/topic")

# Start the loop
client.loop_forever()


