# График поездок


Установка:  
(Питон версии 3)  
создать venv
pip install -r requirements.txt  

RUNNING:  
создать переменную окружения в ENVIRONMENT run, или debug

Пример:

PYTHONUNBUFFERED=1;DEBUG=1;
APP_SETTINGS=config.DevelopmentConfig;
DATABASE_URL=sqlite:///C:/Users/sir/PycharmProjects/taxi-prototype/app.db

set APP_SETTINGS=config.DevelopmentConfig  

python create_test_data.py  
python run.py  


ЗАПУСК С БАЗОЙ POSTGRES:  
sudo su - postgres  
createuser -P taxi  
(set password "taxi")  
createdb -O taxi taxidb  
export APP_SETTINGS=config.StagingConfig  
python manage.py db init  
python manage.py db migrate  
python manage.py db upgrade  
python create_test_data.py  
python run.py  


http://localhost:5000/login  

Коды доступа
login/pass:  
qwerty/qwerty  
asdfgh/asdfgh  
zxcvbn/zxcvbn  

Перевод на русский (не доделано):  
pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot app  
pybabel update -i messages.pot -d app/translations  
pybabel compile -d app/translations  
