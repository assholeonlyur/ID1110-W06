def game():
    import time
    import random
    import cv2
    import cvzone
    from cvzone.HandTrackingModule import HandDetector

    #(380,380) is size for videospace provided in UI
    cap = cv2.VideoCapture(0)


    #Sets width,height of videoframe
    cap.set(3,640)
    cap.set(4,480)

    #Initialize flags
    move = None
    ai_move = 0
    countdown = 0
    Result = False
    startgame = False

    #[AI,Player] scores
    score_tally = [0,0]

    #Ensures only one hand is detected at one time
    detect = HandDetector(maxHands=1)

    while True:

        #Reads and stores bg image in variable
        image_bg = cv2.imread("Rock-Paper-Scissors-Game\Resources\ROCK PAPER SCISSORS.png")

        #Success stores bool, frame stores live video
        success, frame = cap.read()

        #Scale and resize the display vid by 0.791 the actual
        img_scaled = cv2.resize(frame, (0,0), None, 0.791,0.791)

        #Crops the breadth to fit the desired parameter
        #Crops it off from both edges to display center portion
        img_scaled = img_scaled[: , 63:443]

        #Detects hand with help of detector
        hand, img = detect.findHands(img_scaled)

        #Game begins
        if startgame:
            if Result is False:

                #Begins countdown, current time - start time
                countdown = time.time() - init_time

                #Places time value in the desired pixel area; (font, scale, colour, thickness)
                cv2.putText(image_bg,str(int(countdown)),(545,435),cv2.FONT_HERSHEY_DUPLEX, 2, (255,255,255),4)

                if countdown>3:
                    #Resets timer until program is re-run using spacebar
                    Result = True
                    countdown = 0

                    if hand:
                        #If hand is detected, it takes last img of hand before timer stopped
                        hand = hand[0]

                        #gives array of number of fingers up in 0 or 1
                        fingers = detect.fingersUp(hand)
                        if fingers == [0,0,0,0,0]:  #Rock, all fingers down
                            move = 1
                        if fingers == [1,1,1,1,1]:  #Paper, all fingers up
                            move = 2
                        if fingers == [0,1,1,0,0]:  #Scissors, index and mid up
                            move = 3

                        #Plays a move from comp side
                        ai_move = random.randint(1,3)

                        #Displays and overlays the image of corresponding computer result
                        imgAI = cv2.imread(f"Rock-Paper-Scissors-Game\Resources\{ai_move}.png", cv2.IMREAD_UNCHANGED)
                        image_bg = cvzone.overlayPNG(image_bg, imgAI,(75,24))

                        #Human wins, score increment
                        if ((move == 1 and ai_move == 3) or
                            (move == 2 and ai_move == 1) or
                            (move == 3 and ai_move == 2)):
                            score_tally[1] +=1

                        #AI wins, score increment
                        if ((move == 3 and ai_move == 1) or
                            (move == 1 and ai_move == 2) or
                            (move == 2 and ai_move == 3)):
                            score_tally[0] +=1

        #Sets the videofeed on the background
        image_bg[262:642, 680:1060] = img_scaled

        if Result:
            #Displays and overlays the image of corresponding computer result
            #If result is True
            imgAI = cv2.imread(f"Rock-Paper-Scissors-Game\Resources\{ai_move}.png", cv2.IMREAD_UNCHANGED)
            image_bg = cvzone.overlayPNG(image_bg, imgAI,(75,245))

        #Updated score tally is displayed
        cv2.putText(image_bg,str(score_tally[0]),(375,180),cv2.FONT_HERSHEY_DUPLEX, 2, (255,255,255),4)
        cv2.putText(image_bg,str(score_tally[1]),(1000,180),cv2.FONT_HERSHEY_DUPLEX, 2, (255,255,255),4)

        #Displays bg img with all inputs(video,score etc.)
        cv2.imshow("RPS Game", image_bg)

        #Updates image every milisecond, makes it look like a video
        key = cv2.waitKey(1)

        #Spacebar to start the timer and game
        if key == 32:
            startgame = True
            Result = False

            #Notes initial time upon starting the game
            init_time = time.time()


        #Esc key to exit the game
        if key == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
