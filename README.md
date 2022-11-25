# csv parser


## Task

* Создать проект на Django.
* Создать модель с полями охватывающими столбцы из CSV файла.
* Создать страницу с формой, в которую будет загружаться CSV файл.
* Создать View, которая будет парсить этот файл в созданную модель.
* Вывести на отдельную страницу список выгруженных данных.

## How to use
* Начальный экран
![Image alt](static/Screenshot from 2022-11-25 15-07-35.png)
* Необходимо ввести описание файла, и путь к файлу, нажать кнопку "Загрзить"
![](static/Screenshot from 2022-11-25 15-08-10.png)
* Сообщение об успешной загрузке файла, и получение формы для парсинга по полям загруженного .csv файла
![](static/Screenshot from 2022-11-25 15-09-05.png)
* Выгрузка из .csv по заданному значению
![](static/Screenshot from 2022-11-25 15-09-52.png)
![](static/Screenshot from 2022-11-25 15-10-08.png)
* Сообщение об успешной загрузке
![](static/Screenshot from 2022-11-25 15-10-26.png)
* Данные из парсинга сохраняются в БД SQLite
![](static/Screenshot from 2022-11-25 15-11-12.png)
* Так же загружаемые фалы .csv сохраняются в БД
![](static/Screenshot from 2022-11-25 15-11-59.png)
## Tech Stack

The project is currently running on the following versions:

Backend:
* Python 3.10
* Django 4.1.3
* Pandas 1.5.2
* SQLAlchemy 1.4.44

Frontend:
* Bootstrap 5.2.2

## Running Locally

To run the project locally first you need to clone the repository:
```
git clone https://github.com/MrRom4ke/csv_parser.git
```
Create a virtualenv:
```
virtualenv venv -p python3
```
Install the development requirements:
```
pip install -r requirements.txt
```
Run the local server:
```
python3 manage.py runserver
```
## License
The source code is released under the [MIT License](https://github.com/vitorfs/parsifal/blob/master/LICENSE).
## Author
MrRom4ke
