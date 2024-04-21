NUCLEAR HACK SMOKER DETECTION DEMO

Для запуска нужно установить зависимости из requirements.txt: ultralytics и streamlit

Команда для запуска:
```
streamlit run main.py
```

На главной странице - демо с распознаванием позы на основе YOLOv8-pose. Планировалось, что добавим в параллель как параллельный критерий детекцию дистанции между кистями рук и головой, но не успели интегрировать это с обычным обнаружением объектов.

На странице smoker detection - демо с распознаванием курильщика с помощью object detection с помощью YOLOv8. Осуществляется детекция 4 классов:
* Человек
* Сигарета (оч плохо)
* Сигарета в руках
* Сигарета во рту

Ссылка на собранный датасет: https://drive.google.com/drive/folders/1FNRDipUq6ECY8q70gytrVNdRCLzu0pJq?usp=sharing

Ссылка на презентацию: https://docs.google.com/presentation/d/1tJWZQ99HdW8P53Ogf5wAVamw8PqL9pKf/edit?rtpof=true&sd=true
