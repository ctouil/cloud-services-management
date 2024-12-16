#!/usr/bin/env python
import os
import sys
#from backend.settings import *  # Importation absolue

def main():
    """Point d'entrée principal pour les commandes en ligne Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Assurez-vous qu'il est installé "
            "et disponible dans votre environnement virtuel."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
