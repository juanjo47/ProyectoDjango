FROM python:3.8

RUN apt-get update && \
    apt-get install -y python3-dev && \
    pip install --upgrade pip

ENV PYTHONUNBUFFERED=1
# Establecer directorio de trabajo
RUN mkdir /code
WORKDIR /code

# Copiar el archivo de requisitos al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install -r requirements.txt && \
    pip install drf_yasg

# Ejecutar comandos de gestión de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]