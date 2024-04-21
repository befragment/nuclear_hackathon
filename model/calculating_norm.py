from ultralytics import YOLO
import numpy as np

FIRST_WRIST_INDEX = 9
SECOND_WRIST_INDEX = 10

model = YOLO('yolov8m-pose.pt')

img = 'kmz_dataset_5cls_p1/roboto_2_dataset/images/smoking_0188_jpg.rf.d222e71fd1b8f565b99ff0bf0f47dc45.jpg'
img2 = 'images.jpeg'



"""
tensor([[[  0.0000,   0.0000], - нос
         [  0.0000,   0.0000], - правый глаз
         [  0.0000,   0.0000], - левый глаз 
         [  0.0000,   0.0000], - ухо лево
         [ 89.6097,  80.3491], - ухо право
         [ 61.1186,  95.5384], - плечо 1
         [ 99.7691,  95.2791], - плечо 
         [ 50.6663,  68.0840], - локоть
         [112.9486,  69.8895], - локоть
         [ 54.0025,  41.4610], - кисть 1 [9]
         [104.1344,  42.1522], - кисть 2 [10]
         [ 68.8185, 160.6259], ===== ноги
         [ 93.6261, 159.7968],
         [ 72.5943, 204.8244],
         [ 93.0849, 202.1714],
         [ 67.0658, 247.1568],
         [ 97.2070, 246.1048]]]) 
"""


def distance_between_arm_and_nose(img_path: str):
    model(
        source=img2, show=True,
        conf=0.3, save=True
    )

    results = model.track(img_path)
    keypoints_in_pixel = results[0].keypoints.xy[0] # координаты различных частей тела
    nose = keypoints_in_pixel[0].numpy() # координаты keypoint носа
    first_arm_coords = keypoints_in_pixel[FIRST_WRIST_INDEX].numpy() # координаты keypoint одной кисти
    second_arm_coords = keypoints_in_pixel[SECOND_WRIST_INDEX].numpy() # координаты keypoint другой гисти

    norms = list() # список в который добавляем два расстояния (от одной кисти до носа и от другой)

    if first_arm_coords.any() and nose.any():   
        norms.append(np.linalg.norm(first_arm_coords - nose)) # добавляем расстояние от носа до кисти
    if second_arm_coords.any() and nose.any():
        norms.append(np.linalg.norm(second_arm_coords - nose)) # добавляем расстояние от носа до др гисти
        
    result_norm = min(norms) # сигарета в кисти ближайшей к носу ??????

    return result_norm



dist = distance_between_arm_and_nose(img)
print(f"dist: {dist}")