#pixels of images treated as numpy array
#matrix of picture me show kar sakte hai ham 
import os.path
import skimage as sk
import imread
import data_dir
img = imread("C:\Users\Akash Keote\Pictures\Screenshots\Screenshot (1).png")
import matplotlib.pyplot as plt
plt.imshow(img)
print(img)
print(type(img))
print(img.ndim)
print(img.shape)