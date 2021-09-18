# uploadproj
Выполнение тестового задания для поступления на курс ШИФТ Python ML.
_____________________________
Проект newproject представляет собой приложение newapp - простой веб-сервис на Python, позволяющий загрузить изображение,
определить, какие пиксели на нем преобладают - черные или белые, а также определить по HEX коду цвета количество пикселей данного цвета.

При написании использовался фреймворк Django 3.2.7, Python 3.9. Среда разработки - PyCharm 2020.3 (Edu).

Зависимости определены в файле requirements.txt.

Реализовано JSON-логирование в файл jslogs.json.
_____________________________
Для запуска:

git clone https://github.com/aDavletkilldv/uploadproj.git &
cd uploadproj &
pip install -r requirements.txt &
python manage.py migrate &
python manage.py runserver
