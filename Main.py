import tensorflow as tf
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

datadir = "D:/Programming/Banana_Ripeness/Data/"
categories = ["Riped", "Unriped"]
training_data = []
size = 70
X = []
y = []

def create_training_data():
    for category in categories:
        path = datadir + category
        class_num = categories.index(category)
        for img in os.listdir(path):
            img_array = cv2.imread(path + '/' + img)
            rgb = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
            new_array = cv2.resize(rgb, (size,size))
            training_data.append([new_array, class_num])

create_training_data()
random.shuffle(training_data)
for features, label in training_data:
    X.append(features)
    y.append(label)