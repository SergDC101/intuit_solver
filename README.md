## Описание

Скрипт автоматически проходит Экзамен экстерном, ответы берутся из базы данного ресурса https://vtone.ru/

Во время теста делаются скиншоты и сохраняются в папку указаную в `.env`, затем формируется `.docx` файл с колонтитулами

## Для запуска необходимо

* Python 3.13 или новее
* Google Chrome браузер
* Подписаться на необходимый курс на интуите

## Шаги для запуска

1) Создать виртуальное окружение в папке проекта

   **На Windows:**

    ```commandline
    # Создание виртуального окружения
    python -m venv myenv
    
    # Активация
    myenv\Scripts\activate
    ```

   **На Linux/MacOS:**

    ```commandline
    # Создание виртуального окружения
    python3 -m venv myenv
    
    # Активация
    source myenv/bin/activate
    ```


2) Установить зависимости

    ```commandline
    pip install -r .\requirements.txt
    ```


3) Создать файл `.env` в корне директории проекта

    Пример `.env` файла:
    
    ```dotenv
    INTUIT_LOGIN=user@user.ru
    INTUIT_PASSWORD=user
    EXAM_EXTERN_COURSE_LINK=https://intuit.ru/studies/courses/17/17/test/4/0
    ABSOLUT_PATH=C:\Users\user\OneDrive\Desktop\intuit
    STUDENT_NAME='Иванов Иван'
    GROUP_NAME=ВПИ-99
    ```

   - **INTUIT_LOGIN** - логин от Intuit
   - **INTUIT_PASSWORD** - пароль от Intuit
   - **EXAM_EXTERN_COURSE_LINK** - ссылка на [Экзамен экстерном](https://intuit.ru/studies/courses/17/17/test/4/0)
   - **ABSOLUT_PATH** - абсолютный путь до папки для сохранения файлов (Windows:
     `C:\Users\user\OneDrive\Desktop\intuit`, Linux: `/home/user/intuit/`)
   - **STUDENT_NAME** - ФИО для коллонтитулов
   - **GROUP_NAME** - номер группы для коллонтитулов


4) Запустить main.py
    ```commandline
    python main.py
    ```

5) По завршениею теста необходимо зайти на страницу экзамена, и завершить его (если устраивает кол-во баллов), и скачать сертификат.