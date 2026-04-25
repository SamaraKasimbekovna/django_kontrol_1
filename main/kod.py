# 1 Активировать виртуальную среду
source myenv/bin/activate

# 2 Проводим фиксацию наших настроек
python manage.py migrate (изменение в настройках необходимо зафиксировать)

python manage.py makemigrations


# 3 Запустить сервер
python manage.py runserver

# 
python manage.py startapp (app_name (создание приложения)  

python manage.py createsuperuser (создание суперпользователя)     

1.git init
2.git add .
3.git commit -m "first commit"
4.git branch -M main
5.git remote add origin <repository_url>(git remote add origin https://github.com/USERNAME/REPO.git)
6.git push -u origin main


ДАЛЬШЕ (каждый раз при изменениях)

git add .
git commit -m "Домашка №7"
git push