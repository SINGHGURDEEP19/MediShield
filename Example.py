import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = '/Users/gurdeepsingh/Downloads/AgriCare-Detect-master/Dataset/Original Images/BacterialSpot/BacterialSpot(396).jpg'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

plant = cv2.imread('/Users/gurdeepsingh/Downloads/AgriCare-Detect-master/Dataset/test/___Bacterial_spot (1).JPG')
test_image = cv2.resize(plant, (128,128)) # load image 
  
test_image = img_to_array(test_image)/255 # convert image to np array and normalize
test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
result = model.predict(test_image) # predict diseased palnt or not
  
pred = np.argmax(result, axis=1)
print(pred)
if pred==0:
    print( "Bacteria Spot Disease")
       
elif pred==1:
    print("Early Blight Disease")
        
elif pred==2:
    print("Healthy and Fresh")
        
elif pred==3:
    print("Late Blight Disease")
       
elif pred==4:
    print("Leaf Mold Disease")
        
elif pred==5:
    print("Septoria Leaf Spot Disease")
        
elif pred==6:
    print("Target Spot Disease")
        
elif pred==7:
      print("Yellow Leaf Curl Virus Disease")
elif pred==8:
      print("Tomato Mosaic Virus Disease")
        
elif pred==9:
      print("Two Spotted Spider Mite Disease")
