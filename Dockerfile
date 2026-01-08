#Imagen base con Python
FROM python:3.12-slim

#Crear directorio de trabajo dentro del contenedor
WORKDIR /app

#Copiar requirements primero (optimización de cache)
COPY requirements.txt .

#Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Copiar el resto del código
COPY ./app ./app

#Exponer el puerto
EXPOSE 8000

#Comando para ejecutar la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
