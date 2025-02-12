# Projects in Data Science (2025)

This project focuses on analyzing a dataset containing images of human skin with visible lesions. The primary objective is to determine whether these skin lesions may indicate the presence of cancer or if they result from genetic factors, injury, or other conditions.

We begin by defining skin lesions as areas of the skin that differ in appearance from the surrounding tissue. Skin lesions are common and can arise due to various causes, including injury, genetic predisposition, infections, or autoimmune diseases. In some cases, they may also serve as early indicators of serious conditions, such as skin cancer.

As part of our analysis, we quantify the number of hairs present in each image from the dataset. Additionally, we preprocess the images by removing hair to enhance the clarity of the lesions. This step enables more effective identification and classification of skin lesions, facilitating the distinction between those associated with potential diseases and those caused by genetic or external factors.

In the data, we individually assesed the amount of hair in the images provided. We calculated the amount of 0s (no hair), 1s (little hair), and 2s (lots of hair). 

The computation gave us results: 
Anis annotated 62 pictures as '0', 83 pictures as '1' and 55 pictures as '2'.
Anna annotated 44 pictures as '0', 46 pictures as '1' and 10 pictures as '2'.
Julia annotated 51 pictures as '0', 40 pictures as '1' and 24 pictures as '2'.
Laura annotated 50 pictures as '0', 41 pictures as '1' and 22 pictures as '2'.
Lukas annotated 42 pictures as '0', 52 pictures as '1' and 12 pictures as '2'.

Looking at the rating mode of each picture, there were 78 images with no hair (0), 75 images with little hair (1) and 45 images with lots of hair (2). Two images had conflicting annotations, which led to an error in calculating the mode.

Hair Segmentation Examples

In step three of our project we segmented hair with TELEA method, based on the template code from the lecture. Below are examples of visually successful and unsuccessful results:
Good Visual Results
![Example of good segmentation 1](result/output1739.jpg)
![Example of good segmentation 2](result/output1757.jpg)

Poor Visual Results
![Example of poor segmentation 1](result/output1721.jpg)
![Example of good segmentation 2](result/output1730.jpg)