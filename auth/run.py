import os
from decouple import config

port = config('API_PORT')


os.system(f'python manage.py runserver {port}')