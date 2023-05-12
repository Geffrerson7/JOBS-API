# JOBS-API

## Descripción
API para monitorear tus postulaciones de trabajo.

## ERD

![ERD-JOB-API](https://github.com/Geffrerson7/JOBS-API/assets/61089189/3872c61c-23e5-49ee-9243-cfc73bdc57ed)

## Instalación local del proyecto

Clonar el repositorio

```bash
$ git clone https://github.com/Geffrerson7/JOBS-API-.git
```

Ir al directorio al proyecto

```bash
$ cd JOBS-API
```

Crear un entorno virtual

```sh
$ virtualenv venv
```
Activar el entorno virtual
```sh
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Luego, realizamos las migraciones.
```sh
(env) $ python manage.py makemigrations
```
```sh
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app
```sh
(env)$ python manage.py runserver
```
Y navegar a
```sh
http://127.0.0.1:8000/
```

## Instalación en Docker del proyecto

Clonar el repositorio

```bash
$ git clone https://github.com/Geffrerson7/JOBS-API.git
```

Ir al directorio al proyecto

```bash
$ cd JOBS-API
```

Ejecutar el comando
```sh
$ docker-compose up
```

Y navegar a
```sh
http://127.0.0.1:8000/
```

## Tecnologías y lenguajes utilizados

* **Python** (v. 3.10.7) [Source](https://www.python.org/)
* **Django** (v. 4.2)  [Source](https://www.djangoproject.com/)
* **Django Rest Framework** (v. 3.14.0) [Source](https://www.django-rest-framework.org/)
* **django-cors-headers** (v. 3.14.0) [Source](https://pypi.org/project/django-cors-headers/)
* **Simple JWT** (v. 5.2.2) [Source](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* **drf-yasg** (v. 1.21.5) [Source](https://drf-yasg.readthedocs.io/en/stable/)

## Enlace de la aplicación Frontend del proyecto

[![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=github)](https://github.com/Geffrerson7/JOBS-API-FRONTEND)

## Autor
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)
