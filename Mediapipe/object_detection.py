# --------------> IMPORT LIBRARIES
import cv2
import urllib.request
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt

# --------------> SETUP MEDIAPIPE OBJECTRON
mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils

# --------------> HELPER FUNCTION TO LOAD IMAGE FROM URL
def url_to_array(url):
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

# --------------> LOAD IMAGE
image_url = 'https://media.istockphoto.com/id/1279108197/photo/variety-of-womens-fashion-comfortable-shoes-of-all-seasons-on-a-light-background-top-view.jpg?s=2048x2048&w=is&k=20&c=jWiosldK02nugxrR-KxBJ9Y4xXzS6JNyG6wCK4jSDSI='
input_image = url_to_array(image_url)

# --------------> INSTANTIATE OBJECTRON
with mp_objectron.Objectron(
    static_image_mode=True,
    max_num_objects=5,
    min_detection_confidence=0.5,  # Increased for better precision
    model_name='Shoe'  # Changed to 'Shoe' to match the image content
) as objectron:

    results = objectron.process(input_image)

    # --------------> CHECK FOR DETECTIONS
    if not results.detected_objects:
        print('❌ No 3D objects detected.')
    else:
        annotated_image = input_image.copy()
        for obj in results.detected_objects:
            mp_drawing.draw_landmarks(
                annotated_image,
                obj.landmarks_2d,
                mp_objectron.BOX_CONNECTIONS
            )
            mp_drawing.draw_axis(
                annotated_image,
                obj.rotation,
                obj.translation
            )

        # --------------> DISPLAY RESULT
        plt.figure(figsize=(10, 10))
        plt.imshow(annotated_image)
        plt.axis('off')
        plt.title('Detected 3D Objects')
        plt.show()
