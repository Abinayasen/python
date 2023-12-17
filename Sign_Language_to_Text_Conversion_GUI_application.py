import numpy as np
import math
import cv2
import os
import pyttsx3
from keras.models import load_model
from cvzone.HandTrackingModule import HandDetector
from string import ascii_uppercase
import enchant
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

OFFSET = 29
MODEL_PATH = '/cnn8grps_rad1_model.h5'

class SignLanguageConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Language to Text Converter")
        self.root.geometry("1536x864")

        # Initialize HandDetectors
        hd = HandDetector(maxHands=1)
        hd2 = HandDetector(maxHands=1)

        # Other Variables
        self.str = " "
        self.ten_prev_char = [" "] * 10
        self.words = ['HELLO', 'WORLD', 'GOOD', 'MORNING']
        self.word = self.words[0]

        # Load the model
        self.model = load_model(MODEL_PATH)

        # Configure widgets
        self.T = Label(root)
        self.T1 = Label(root)
        self.b1 = Button(root)
        self.b2 = Button(root)
        self.b3 = Button(root)
        self.b4 = Button(root)

        # Load white image
        white_path = os.path.join("C:\\Users\\devansh raval\\PycharmProjects\\pythonProject\\white.jpg")
        white = cv2.imread(white_path)

        # Other widget configurations
        self.T.config(text="Sign Language To Text Conversion", font=("Courier", 30, "bold"))
        self.T1.config(text="Character :", font=("Courier", 30, "bold"))
        self.b1.config(text=self.words[0], font=("Courier", 20), wraplength=825, command=lambda: self.update_str(0))
        self.b2.config(text=self.words[1], font=("Courier", 20), wraplength=825, command=lambda: self.update_str(1))
        self.b3.config(text=self.words[2], font=("Courier", 20), wraplength=825, command=lambda: self.update_str(2))
        self.b4.config(text=self.words[3], font=("Courier", 20), wraplength=825, command=lambda: self.update_str(3))

        # Other initialization logic...

    def update_str(self, index):
        idx_space = self.str.rfind(" ")
        idx_word = self.str.find(self.word, idx_space)
        last_idx = len(self.str)
        self.str = self.str[:idx_word] + self.words[index].upper()

    # Other methods...

if __name__ == "__main__":
    root = Tk()
    app = SignLanguageConverter(root)
    root.mainloop()

