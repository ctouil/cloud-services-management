import os

# Chargement des paramètres de configuration du projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',  # Ajoutez ici votre application
]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'cloud_management_db',
    }
}

# Définition des hôtes autorisés
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Remplacez par vos hôtes réels si nécessaire
