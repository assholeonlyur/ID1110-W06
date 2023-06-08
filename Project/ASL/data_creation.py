import os
import pickle
import cv2
import mediapipe as mp

#Drawing function on hands initialization
drawing = mp.solutions.drawing_utils
drawing_styles = mp.solutions.drawing_styles

#Initialise hands class
hand = mp.solutions.hands

data, labels = [],[]
data_folder = './ASL/data'

#Sets up hand detection, if comp is sure above 30% then it reads image as hand
hands = hand.Hands(static_image_mode=True, min_detection_confidence=0.3)

for dir_ in os.listdir(data_folder):
    for img_path in os.listdir(os.path.join(data_folder, dir_)):
        #Reads through every image
        hand_data, x_, y_ = [], [], []

        img = cv2.imread(os.path.join(data_folder, dir_, img_path))

        #Converts image to RGB format from BGR, coz cv2 by default changes all to BGR
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #Checks if handmarks are detected then iterates through them all 
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    #Saves x,y coordinate of every handpoint as array
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    #For normalisation of dataset, takes only distance between data
                    hand_data.append(x - min(x_))
                    hand_data.append(y - min(y_))

            data.append(hand_data)
            labels.append(dir_)

#Makes a binary file with data of every handmark corresponding to its label(A/B/C/....)
file = open('./ASL/data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, file)
file.close()
