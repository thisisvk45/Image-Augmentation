#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import cv2
import numpy as np
import random


# In[ ]:


original_root_folder = r'C:\Users\Plaksha\Desktop\Sem 5\MLPR\Project\Original'
augmented_root_folder = r'C:\Users\Plaksha\Desktop\Sem 5\MLPR\Project\Augmented'


# In[24]:


num_augmented_images = 100

os.makedirs(augmented_root_folder, exist_ok=True)

for original_subfolder in os.listdir(original_root_folder):
    original_subfolder_path = os.path.join(original_root_folder, original_subfolder)
    
    if os.path.isdir(original_subfolder_path):
        augmented_subfolder = os.path.join(augmented_root_folder, f'Augmented_{original_subfolder}')
        os.makedirs(augmented_subfolder, exist_ok=True)

        for i in range(num_augmented_images):
            original_images = [f for f in os.listdir(original_subfolder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
            if original_images:
                original_image_file = random.choice(original_images)
                original_image_path = os.path.join(original_subfolder_path, original_image_file)
                original_image = cv2.imread(original_image_path)

                if original_image is not None:
                    brightness_factor = random.uniform(0.5, 1.5)
                    augmented_image = cv2.convertScaleAbs(original_image, alpha=brightness_factor, beta=0)

                    angle = random.uniform(-30, 30)
                    height, width = augmented_image.shape[:2]
                    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
                    augmented_image = cv2.warpAffine(augmented_image, rotation_matrix, (width, height))

                    augmented_image_path = os.path.join(augmented_subfolder, f'augmented_{i}.jpg')
                    cv2.imwrite(augmented_image_path, augmented_image)
                else:
                    print(f"Failed to load image: {original_image_path}")
            else:
                print(f"No image files found in: {original_subfolder_path}")

print(f'{num_augmented_images} augmented images have been created for each subfolder in the "Original" directory and saved in corresponding subfolders in the "Augmented" directory.')


# In[ ]:




