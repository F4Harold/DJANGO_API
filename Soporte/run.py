import os
from decouple import config

#leer el puerto .env
port = config('API_PORT')

#ejecutar el servidor django

os.system(f'python manage.py runserver {port}')