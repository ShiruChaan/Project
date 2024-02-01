This document provides detailed instructions for deploying the Django project using Docker and Docker Compose, including setting up a MySQL database and creating a superuser for Django admin.

## Prerequisites

Before you begin, ensure you have the following installed on your server:

- Docker
- Docker Compose

## Project Setup

1. **Clone the Repository**: Clone your project repository to your server.

    ```bash
    git clone <your-repository-url>
    cd <your-project-directory>
    ```

2. **Environment Variables**: Set up the necessary environment variables in your `docker-compose.yml` file.

## Docker Compose Setup

Replace `yourdbname`, `yourdbuser`, `yourdbpassword`, and `rootpassword` with preferred database name, user, password, and MySQL root password. These will be used to create new MySQL container.

### Sample `docker-compose.yml`

```yaml
version: '3.8'

services:
  web:
    build: .
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/usr/src/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DB_NAME=yourdbname
      - DB_USER=yourdbuser
      - DB_PASS=yourdbpassword
      - DB_HOST=db

  db:
    image: mysql:5.7
    volumes:
      - mysql_data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: yourdbname
      MYSQL_USER: yourdbuser
      MYSQL_PASSWORD: yourdbpassword

volumes:
  mysql_data:
```

## Building and Running Containers

Run the following command to build and start your containers:

```bash
docker-compose up --build
```
This command builds the Django application and starts the services defined in your docker-compose.yml.

## Creating a Django Superuser
To create a Django superuser, run the following command:

```bash
docker-compose run web python manage.py createsuperuser
```
Follow the prompts to enter the desired username, email, and password for the superuser.

