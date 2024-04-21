from cProfile import label
from tkinter import image_names
import streamlit as st
import time
import os
import numpy as np
from PIL import Image
from ultralytics import YOLO
from model.calculating_norm import get_last_directory_contents
model = YOLO('yolov8m-pose.pt')


def some_ai_func():
    time.sleep(2)
    print("Success")


def generate_sidebar():
    
    st.sidebar.markdown(
        '# Проект выполнила группа Nuclear: \n'
        '- Богдан Левченко \n'
        '- Евгений Коровин\n'
        '- Петр Рыбаков\n'
        '- Мария\n'
    )
    st.sidebar.markdown("____")

    st.sidebar.markdown(
        '# Инструкция по использованию:\n'
        '1. Загрузите файл с фото или видео в главной части сайта\n'
        '2. Нажмите кнопку ```Вычислить курильщика(ов)```\n'
        '3. Ожидайте, в скором времени очень умная нейросеть скажет вам, курит ли человек на фото'
    )
    st.sidebar.markdown('___')

    st.sidebar.markdown('# Ссылка на Github: [nuclear_hackathon](https://github.com/befragment/nuclear_hackathon)')  # !!!!!!!!!!!!!!!!!!!!!!!!
    

def main():
    generate_sidebar()

    st.title("Nuclear Team WebPage")   
    st.write("____")

    image_file = st.file_uploader(
        label="Переместите фотографии ниже :sunglasses:",
        type=['jpg', 'png', 'jpeg', 'gif'],
        # accept_multiple_files=True,
    )
    original_image = Image.open(image_file)
    original_image_np = np.asarray(original_image).astype(np.uint8)
    button_click = st.button("Вычислить") # returns bool

    images_to_process = []

    with st.spinner("Нейросеть думает..."):
        if button_click:
            # for image in image_files:
            #     images_to_process.append(image.name)
            model(
                # source=images_to_process, show=False,
                source=original_image_np, show=False,
                conf=0.3, save=True
            )

            
            directory = get_last_directory_contents('runs/pose')
            for filename in os.listdir(directory):
                print(filename)
                st.image(f'{directory}/{filename}', caption='pred score')


if __name__ == '__main__':
    main()
