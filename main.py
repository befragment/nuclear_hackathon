import streamlit as st
import time

def some_ai_func():
    time.sleep(2)
    print("Success")


def generate_sidebar():
    
    st.sidebar.markdown(
        '# Проект выполнила группа Nuclear: \n'
        '- Богдан\n'
        '- Евгений\n'
        '- Петр\n'
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

    st.sidebar.markdown('# Ссылка на Github: [SmokingDetection](ВСТАВИТЬ ССЫЛКУ НА РЕПУ)')  # !!!!!!!!!!!!!!!!!!!!!!!!
    

def main():
    generate_sidebar()

    st.title("Nuclear Team WebPage :smoking:")   
    st.write("____")

    image_files = st.file_uploader(
        label="Drag your image here :sunglasses:",
        type=['jpg', 'png', 'jpeg', 'gif'],
        accept_multiple_files=True,
    )

    button_click = st.button("Вычислить пидораса") # returns bool


    with st.spinner("Нейросеть думает..."):
        if button_click:
            some_ai_func()
            for image in image_files:
                st.image(
                    image=image,
                    caption=f"model score is {__import__('random').randint(69, 100)}%!!!"
                )


if __name__ == '__main__':
    main()
