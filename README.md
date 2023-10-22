# Django
 - 1 creamos el entorno virtual  python -m venv nombre_del_entorno
 - 2 activamos el entorno virtual  nombre_del_entorno\Scripts\activate
 - 3  instalamos django pip install django
 - 4 se actualiza pip version de ser necesario python -m pip install --upgrade pip
 - 5 Creamos un nuevo proyecto Django con la estructura de directorios  inicial django-admin startproject nombre_proyecto
 - 6 Inicia el servidor de desarrollo de Django para ejecutar la aplicación en modo de desarrollo python manage.py runserver
 - 7 Creamos una nueva aplicación dentro del proyecto Django  python manage.py startapp nombre_app
 - 8 Vamos a la carpeta del proyecto al archivo settings.py -> INSTALLED_APPS ['nombre de la aplicación']
 - 9 vamos al archivo models.py importamos from django.db import models, from django.contrib.auth.models import AbstractUser
 - 10 agregamos el usuario al archico admin.py y lo configuramos en settings.py  -> UTH_USER_MODEL
 - 11 Creamos archivos de migración basados en los cambios en los modelos de la base de datos  python manage.py makemigrations
 - 12 Aplica las migraciones pendientes para actualizar la base de datos python manage.py migrate
 - 13 Crea un superusuario para acceder al panel de administración de Django python manage.py createsuperuser
 - 14 configuramos el login  con email del super user  desde el archivo models.py
 - 15 Instalamos django-rest-framework https://www.django-rest-framework.org/ y lo  añadimos al archivo settings.py 

