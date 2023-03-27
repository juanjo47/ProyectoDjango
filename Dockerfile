FROM python:3.9

# Establecer directorio de trabajo
WORKDIR /app

# Copiar el archivo de requisitos al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Crear un nuevo directorio para el código de la aplicación
RUN mkdir /app_code
WORKDIR /app_code

# Copiar todo el código de la aplicación al contenedor
COPY . .

# Ejecutar comandos de gestión de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]