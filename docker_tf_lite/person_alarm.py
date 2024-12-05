import numpy as np
import zipfile
import argparse
import sys
import time
import os
import cv2
from object_detector import ObjectDetector
from object_detector import ObjectDetectorOptions
import utils
from utils import labels

class ObjectDetection:

    def __init__(self):    
        self.num_threads = 4
        self.score_threshold = 0.3
        self.max_results = 10

        path_to_model = "model/efficientdet_lite0.tflite"

        try:
            with zipfile.ZipFile(path_to_model) as model_with_metadata:
                if not model_with_metadata.namelist():
                    raise ValueError('Invalid TFLite model: no label file found.')
                
        except zipfile.BadZipFile:
            print(
                'ERROR: Please use models trained with Model Maker or downloaded from TensorFlow Hub.'
            )
            raise ValueError('Invalid TFLite model: no metadata found.')

        # Initialize the object detection model
        options = ObjectDetectorOptions(
            num_threads=self.num_threads,
            score_threshold=self.score_threshold,
            max_results=self.max_results,
            enable_edgetpu=False)

        self.detector = ObjectDetector(labels, path_to_model, options=options)

    def detect_objects(self, image):
        """Run object detection on the provided image."""
        results = self.detector.detect(image)
        return results

def remove_old_alarm(file_path):
    try:
        os.remove(file_path)
        print(f"{file_path} has been removed successfully.")
    except FileNotFoundError:
        print(f"{file_path} does not exist.")
    except PermissionError:
        print(f"Permission denied to delete {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# def main():    
    
#     remove_old_alarm('/home/liran/person_alarm/docker_tf_lite/person.jpeg')

#     # Initialize Object Detection
#     obj_det = ObjectDetection()

#     # Load the image
#     image = cv2.imread('/home/liran/person_alarm/docker_tf_lite/alarm.jpeg',1)
#     if image is None:
#         print("ERROR: Unable to load image.")
#         sys.exit(0)

#     # Perform object detection
#     results = obj_det.detect_objects(image)

    
#     # Loop through detection results
#     for result in results:
#         print(f"{result}")
#         # Check if the category is 'person' and if the score is above the threshold
#         if any(category.label == 'Person' for category in result.categories):
#             print("person detected !!! ")
#             # Draw the bounding box on the image
#             cv2.rectangle(image, 
#                           (result.bounding_box.left, result.bounding_box.top), 
#                           (result.bounding_box.right, result.bounding_box.bottom), 
#                           color=(0, 255, 0), thickness=2)
            
#             # Optional: Add text label with score
#             cv2.putText(image, 
#                         f'Person: {result.categories[0].score:.2f}', 
#                         (result.bounding_box.left, result.bounding_box.top - 10), 
#                         cv2.FONT_HERSHEY_SIMPLEX, 
#                         0.5, 
#                         (0, 255, 0), 
#                         2)
#             print('wrting the image of the person ..')
#             cv2.imwrite('/home/liran/person_alarm/docker_tf_lite/person.jpeg',image)

#     exit(0)



def main():
    try:
        # Remove old alarm image
        remove_old_alarm('/home/liran/person_alarm/docker_tf_lite/person.jpeg')
    except Exception as e:
        print(f"ERROR: Failed to remove old alarm image: {e}")
        sys.exit(0)

    try:
        # Initialize Object Detection
        obj_det = ObjectDetection()
    except Exception as e:
        print(f"ERROR: Failed to initialize ObjectDetection: {e}")
        sys.exit(0)

    try:
        # Load the image
        image = cv2.imread('/home/liran/person_alarm/docker_tf_lite/alarm.jpeg', 1)
        if image is None:
            print("ERROR: Unable to load image.")
            sys.exit(0)
    except Exception as e:
        print(f"ERROR: An error occurred while loading the image: {e}")
        sys.exit(0)

    try:
        # Perform object detection
        results = obj_det.detect_objects(image)

        # Loop through detection results
        for result in results:
            print(f"{result}")
            # Check if the category is 'person' and if the score is above the threshold
            if any(category.label == 'Person' for category in result.categories):
                print("Person detected!!!")
                # Draw the bounding box on the image
                cv2.rectangle(image, 
                              (result.bounding_box.left, result.bounding_box.top), 
                              (result.bounding_box.right, result.bounding_box.bottom), 
                              color=(0, 255, 0), thickness=2)

                # Optional: Add text label with score
                cv2.putText(image, 
                            f'Person: {result.categories[0].score:.2f}', 
                            (result.bounding_box.left, result.bounding_box.top - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            0.5, 
                            (0, 255, 0), 
                            2)
                print('Writing the image of the person...')
                try:
                    cv2.imwrite('/home/liran/person_alarm/docker_tf_lite/person.jpeg', image)
                except Exception as e:
                    print(f"ERROR: Failed to write image: {e}")
                    sys.exit(0)
    except Exception as e:
        print(f"ERROR: An error occurred during object detection: {e}")
        sys.exit(0)

    sys.exit(0)






if __name__ == '__main__':

    main()
