# Import modules
import sys
import os
try:
    #Imports modules if available
    from PyQt5.QtWidgets import *
    import cv2
    import cvzone
    from cvzone.HandTrackingModule import HandDetector
    import mediapipe
    import sklearn
    import numpy


except ModuleNotFoundError:
    #If module isnt downloaded, starts installation
    print("You do not have the necessary modules installed!")
    input("Press any key to start installation!!")

    while True:

        try:
            #Runs the following in command prompt of system
            os.system("py -m pip install --user opencv-python")
            os.system("py -m pip install --user cvzone")
            os.system("py -m pip install --user mediapipe")
            os.system("py -m pip install --user numpy")
            os.system("py -m pip install --user scikit-learn")
            os.system("py -m pip install --user PyQt5")

            #Import after installation
            from PyQt5.QtWidgets import *
            import cv2
            import cvzone
            from cvzone.HandTrackingModule import HandDetector
            import mediapipe
            import sklearn
            import numpy
            print("Modules successfully installed")
            input("Press enter to continue")
            break

        except ModuleNotFoundError:
            #If internet connection isn't there it raises this error
            print("Are you connected to the internet?")
            print("Please check your internet and try again")
            input("Press enter to try again")


# adding both main files to the system path
sys.path.insert(0, "Rock-Paper-Scissors-Game")
sys.path.insert(1, "ASL")

#Import the functions required from other scripts
from main import ASL
from RPS_game import game


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        
        #Makes a push button for both scripts and makes size
        self.pushButton1 = QPushButton("American Sign", self.centralwidget)
        self.pushButton2 = QPushButton("Game", self.centralwidget)
        self.pushButton1.resize(20,30)
        self.pushButton2.resize(20,30)
        self.pushButton1.clicked.connect(self.click1)
        self.pushButton2.clicked.connect(self.click2)

        lay = QHBoxLayout(self.centralwidget)
        lay.addWidget(self.pushButton1)
        lay.addWidget(self.pushButton2)
    def click1(self):
        #Displays message and runs script when first button is clicked
        QMessageBox.about(self, "Warning!!", "Press esc key to exit ASL")   
        ASL()
    def click2(self):
        #Displays message and runs script when second button is clicked
        QMessageBox.about(self, "Warning!!", "Press esc key to exit Game")
        game()

#Background image insertion
stylesheet = """
    MainWindow {
        background-image: url("bg.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    
    #Makes window to display everything
    window = MainWindow()
    window.resize(1200, 900)
    window.show()
    sys.exit(app.exec_())
