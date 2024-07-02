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

Para correr el proyecto con Docker Compose, se debe correr el siguiente comando en la raíz del proyecto:

```bash
docker-compose up
```

Esto creará y correrá el contenedor con la API y la base de datos. A través de la url `http://127.0.0.1:8000` se puede acceder a la API.

## Endpoints

### GET /saludos

Devuelve la lista de saludos existentes en la base de datos.

### POST /saludos

Crea un nuevo saludo en la base de datos. Se debe enviar un JSON con el siguiente formato:

```json
{
    "mensaje": "Hola, mundo!"
}
```

### GET /saludos/{id}

Devuelve el saludo con el id especificado.
