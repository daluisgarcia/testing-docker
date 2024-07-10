# API de saludos

## Preparación de entorno

Para poder correr el proyecto de una forma sencilla, es necesario tener instalado Docker y Docker Compose. Para instalar Docker, se puede seguir la guía oficial [aquí](https://docs.docker.com/get-docker/). Para instalar Docker Compose, se puede seguir la guía oficial [aquí](https://docs.docker.com/compose/install/).

Con Docker y Docker Compose instalados, se puede clonar el repositorio y seguir con los siguientes pasos.

### Creación de archivo override para Docker Compose (opcional)

Debido a que la configuración de Docker Compose está definida para un entorno de producción, se debe crear un archivo `docker-compose.override.yml` en la raíz del proyecto con el siguiente contenido recomendado:

```yaml
services:
  app:
    command: flask run --host=0.0.0.0 --port 5000 --reload
    volumes:
      - .:/api_flask/
```

Esta configuración ejecuta el proyecto en **modo desarrollo** y permite el reinicio de la ejecución al detectar un cambio dentro del código (gracias a la vinculación del volume). Puedes agregar cualquier configuración adicional que necesites en este archivo. **No es recomendable modificar la propiedad `ports`**, ya que puede presentar comportamientos inesperados.

## Correr el proyecto

Para correr el proyecto con Docker Compose, se deben correr los siguientes comandos en la raíz del proyecto:

```bash
docker-compose build
docker-compose up
```

Esto creará y correrá el contenedor con la API y la base de datos. A través de la url `http://127.0.0.1:8000` se puede acceder a la API. Para detener la ejecución, se puede presionar `Ctrl + C` en la terminal. Si deseas correr el proyecto en segundo plano, puedes correr el siguiente comando:

```bash
docker-compose up -d
```

Si deseas ejecutar el proyecto con una configuración de producción, elimina o cambia el nombre del archivo `docker-compose.override.yml` y corre los comandos anteriores.

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

## Despliegue en producción

Para realizar el despliegue en producción, puedes instalar Docker y Docker Compose en tu servidor y seguir los mismos pasos que en tu entorno local sin la necesidad de crear el archivo `docker-compose.override.yml`, ya que la configuración de producción se encuentra en el archivo `docker-compose.yml` y `Dockerfile`.
