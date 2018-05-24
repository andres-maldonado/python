
6
down vote
Install the cors-headers package with

pip install django-cors-headers
Adds to your installed apps

INSTALLED_APPS = (

    ...
    'corsheaders',
    ...
)
Add on your MIDDLEWARE remember to add as being the first in the list

MIDDLEWARE = [  

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
Before installed apps put this configuration for anyone to access

CORS_ORIGIN_ALLOW_ALL=True
Or create a list of hits

CORS_ORIGIN_WHITELIST = (

    'google.com',
    'hostname.example.com',
    'localhost:8000',
    '127.0.0.1:9000'
)
