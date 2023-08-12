import cv2
import os
import tensorflow as tf
from glob import glob
import numpy as np
import matplotlib.pyplot as plt

def iou(y_true, y_pred):
    def f(y_true, y_pred):
        intersection = (y_true * y_pred).sum()
        union = y_true.sum() + y_pred.sum() - intersection
        x = (intersection + 1e-15) / (union + 1e-15)
        x = x.astype(np.float32)
        return x
    return tf.numpy_function(f, [y_true, y_pred], tf.float32)

smooth = 1e-15
def dice_coef(y_true, y_pred):
    y_true = tf.keras.layers.Flatten()(y_true)
    y_pred = tf.keras.layers.Flatten()(y_pred)
    intersection = tf.reduce_sum(y_true * y_pred)
    return (2. * intersection  + smooth) / (tf.reduce_sum(y_true) + tf.reduce_sum(y_pred) + smooth)

def dice_loss(y_true, y_pred):
    return 1.0 - dice_coef(y_true, y_pred)

with tf.keras.utils.CustomObjectScope({'iou':iou, 'dice_coef':dice_coef, 'dice_loss':dice_loss}):
    model = tf.keras.models.load_model("models\\unet_for_skull_stripping.h5")

#process image function
def read_img(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (256, 256))
    img = img / 255
    img = img.astype(np.float32)
    return img

def predict(path):
    images = sorted(glob(os.path.join(path,"*")))
    for i in range(len(images)):
        print(images[i])
        image = read_img(images[i])
        img = image.reshape(1, 256, 256, 3)
        pred = model.predict(img)[0] > 0.5  
        pred = pred.astype(np.int32)
        pred_img = pred.reshape(256, 256, 1)
        cv2.imwrite("static\\predicted\\mask-1.png", pred_img)
        maskImg = cv2.imread("static\\predicted\\mask-1.png")
        maskImg = cv2.cvtColor(maskImg, cv2.COLOR_BGR2GRAY)
        masked = cv2.bitwise_and(image, image, mask=maskImg)
        plt.imsave(f"static\\results\\stripped{i}.png", masked)
        message = "Done"
    
    return message