
# Skull Stripping 

Skull stripping, also known as brain extraction or brain masking, is the process of removing non-brain tissues from neuroimaging data, leaving only the brain region for further analysis. It is an essential step in various applications, including brain segmentation and connectivity analysis. I have implemented skull stripping using the U-Net architecture, a popular deep learning model for image segmentation. The U-Net consists of an encoder-decoder structure that learns to predict the brain region given an input MRI image. By training the U-Net on a dataset of brain images with corresponding skull masks, the model learns to accurately segment the brain region. During the inference phase, the trained model takes an MRI image as input and generates a binary mask where the brain is marked as foreground and non-brain regions, such as the skull, are marked as background. This mask is then used to extract the brain region from the original image.


# Dataset
I used brain tumor dataset from kaggle and i created this dataset. This dataset contains brain MRI images and its masks. I used Label Studio to create mask. In my dataset, 722 MRI images and 722 masks for brain images. image size is 512x512 but i converted it into 256x256. 

# Model
 * U-NET

# Mask Prediction



## Images and Mask

![App Screenshot](https://github.com/MorningStarTM/skull-stripping/blob/main/images/u1.PNG?raw=true)

## Brain image and Mask
![App Screenshot](https://github.com/MorningStarTM/skull-stripping/blob/main/images/u2.PNG?raw=true)



## Brain Image - True Mask - Predicted Mask
![App Screenshot](https://github.com/MorningStarTM/skull-stripping/blob/main/images/u5.PNG?raw=true)

![App Screenshot](https://github.com/MorningStarTM/skull-stripping/blob/main/images/u7.PNG?raw=true)


## Brain Image - Mask - Stripped Brain
![App Screenshot](https://github.com/MorningStarTM/skull-stripping/blob/main/images/u3.PNG?raw=true)

![App Screenshot](https://github.com/MorningStarTM/skull-stripping/blob/main/images/u4.PNG?raw=true)

![App Screenshot](https://github.com/MorningStarTM/skull-stripping/blob/main/images/u6.PNG?raw=true)

![App Screenshot](https://github.com/MorningStarTM/skull-stripping/blob/main/images/u8.PNG?raw=true)