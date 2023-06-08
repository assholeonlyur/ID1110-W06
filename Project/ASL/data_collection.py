import os
import cv2

#Makes a folder if not exists
data_folder = './ASL/data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

#Number of letters it reads and images for each image
no_of_img = 50
classifiers = 3

#Captures video continuously
cap = cv2.VideoCapture(0)

for j in range(classifiers):
    #Make a folder 0 for first letter and so on
    if not os.path.exists(os.path.join(data_folder, str(j))):
        os.makedirs(os.path.join(data_folder, str(j)))

    print('Collecting data for classifier {}'.format(j))

    while True:
        #Success stores bool, frame stores live video
        success, frame = cap.read()
        cv2.putText(frame, 'Press Spacebar to start', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('Frame', frame)
        #Starts image capture when SpaceBar is pressed
        if cv2.waitKey(25) == 32:
            break

    counter = 0
    while counter < no_of_img:
        success, frame = cap.read()
        cv2.imshow('Frame', frame)
        cv2.waitKey(25)

        #Writes the image, every 25ms into the respective folder, numbers 0-no.of.img
        cv2.imwrite(os.path.join(data_folder, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

#closes window when done taking image for dataset
cap.release()
cv2.destroyAllWindows()
