# Proyecto en django Aitor
## Cosas necesarias

- Guardar las imágenes en **/static** (se cambia en models.py).
- Mostrar las imágenes en **index.html**.
- Aplicar *"blur"* a las áreas rectangulares delimitadas (aplicar el blur con python, la selección de las áreas se hace con JS).
- Buscar una **librería de JS** que permita seleccionar las áreas rectangulares con el ratón. **(JCrop)**
- Las migraciones se hacen con 2 comandos, primero con **python3 manage.py makemigrations images_app** (en este caso es python3 porque la hice en el mac) y **python3 manage.py migrate**. (Si no se hacen las migraciones, a la hora de subir un archivo, se subirá pero dará un error de que la tabla no existe en la base de datos.)