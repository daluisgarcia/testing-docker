# API de saludos

## Preparación de entorno

Para poder correr el proyecto es necesario crear un archivo `.env` en la raíz del proyecto con el contenido de `.env.example` y modificar los valores de las variables de entorno con los valores correspondientes a la base de datos local. El proyecto utiliza una base de datos MySQL.

Es importante tener instalado Docker para poder correr el proyecto y MySQL corriendo con una base de datos creada para poder correr el proyecto sin errores.

## Correr el proyecto

Teniendo Docker instalado, correr el siguiente comando en la raíz del proyecto para crear la imagen:

```bash
docker build -t saludos-api .
```

Para crear y correr el contenedor correr el siguiente comando:

```bash
docker run -p 8000:8000 saludos-api
```

Una vez que el contenedor esté corriendo, se puede acceder a la API en `http://127.0.0.1:8000`.

## Docker Compose

Este proyecto aún no es estable con docker-compose. Se está trabajando en ello.

## Endpoints

### GET /saludo

Devuelve la lista de saludos existentes en la base de datos.

### POST /saludo

Crea un nuevo saludo en la base de datos. Se debe enviar un JSON con el siguiente formato:

```json
{
    "mensaje": "Hola, mundo!"
}
```

### GET /saludo/{id}

Devuelve el saludo con el id especificado.
