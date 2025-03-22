
# Examen Técnico para Desarrollador Junior



Parte 2 del examen con los ejercicios prácticos.


## Desarrollo
### 1. Django
Para hacer funcionar el primer ejercicio hay que seguir los siguientes pasos:

1. Crear proyecto de Django
```bash
  django-admin startproject biblioteca
```

2. Crear app dentro del proyecto

```bash
  django-admin startproject bibliotecaApp
```

3. Registrar la app en settings.py
4. Definir los modelos como se propone en models.py
5. Realizar y aplicar las migraciones
```bash
  python manage.py makemigrations
  python manage.py migrate
```

6. Registrar los modelos en admin.py
7. Crear un usuario admin
```bash
  python manage.py createsuperuser
```
8. Ejecutar el servidor
9. Abrir el navegador con la siguiente URL
```bash
http://127.0.0.1:8000/admin/
  
```
10. Iniciar sesión con el usuario admin

####

De esta manera se puede visualizar el modelo propuesto.

### 2. Python

Para ejecutar los scripts realizados en python basta con tener python instalado y ejecutarlos en la consola de la siguiente manera:

```bash
py countWords.py
py orderNumbers.py
  
```

### 3. MySQL

Las sentencias de SQL pueden copiarse y pegarse en la linea de comandos de MySQL para crear la tabla junto con sus registros.

### 4. API

Para el proyecto en Django de la API hay que seguir pasos similares al primer ejercicio:

1. Crear proyecto de Django

```bash
django-admin startproject tareasApi
```

2. Crear app dentro del proyecto

```bash
django-admin startproject tareas
```

3. Registrar la app en settings.py
4. Definir los modelos como se propone en models.py
5. Realizar y aplicar las migraciones
6. Instalar Django REST Framework
```bash
pip install djangorestframework
```
7. Registrar djangorestframework en settings.py
8. Crear serializador como se propone en serializers.py
9. Crear vistas.
10. Configurar URL's
11. Ejecutar servidor
12. Probar endpoints en navegador web
#
El endpoint tarea_list permite consultar tareas y crear tareas mediante los métodos GET y POST respectivamente.

El endpoint tarea_detail permite actualizar tareas y borrar tareas mediante los métodos PUT y DELETE respectivamente.

Cualquier petición de método HTTP se debe realizar mediante JSON.


## Authors

- [@Humberto Vazquez](https://github.com/RubberBoyVz)

