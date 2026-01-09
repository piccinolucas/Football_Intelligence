FROM jupyter/pyspark-notebook:latest

USER root

WORKDIR /app

# Requerimientos
COPY requirements.txt .

# Instalamos librerías desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ajustamos permisos
RUN chown -R jovyan:users /app

USER jovyan