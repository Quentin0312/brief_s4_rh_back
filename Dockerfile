# Utilisez une image de base Python avec WSGI
FROM python:3.9-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de dépendances dans le conteneur
COPY requirements.txt .

# Installe les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie le code source dans le conteneur
COPY . .

# Expose le port sur lequel le service Hug sera exécuté (par défaut 8000)
EXPOSE 8000

# Définit la commande par défaut pour exécuter le service Hug via WSGI
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:__hug_wsgi__"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server:__hug_wsgi__"]
