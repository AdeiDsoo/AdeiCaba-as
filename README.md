# PythonApp- Adei Dsoo Cabañas González

1. Inicia con una pantalla de bienvenida con una navbar con cuatro botones
2. Navegacion: 
 - PythonApp, te lleva al inicio. 
 - Usuarios, te lleva a una vista de una tabla de los usuarios de la BD con sus diversos atributos donde hay un input para realizar una busqueda en la misma base de datos de usuarios por email.
 Tambien encontraras un boton que dice crear usuario al darle click te llevara a una vista con un form para crear usuario si asi lo deseas al rellenar los campos y darle clic en enviar te redireccionará nuevamente a la tabla de usuarios donde podrás apreciar el la lista con el nuevo usuario creado. En caso de decidir no crear usuario y darle clic a cancelar te devolvera a la pantalla de incio de la app. 
 - Cursos, te redirecciona a una pantalla donde renderiza los cursos existentes en la base de datos en caso de no tener cursos la BD igualmente muestra un letrero de 'no se entruentran cursos registrados en este momento'. Esta vista tambien cuenta con un boton para crear curso que te lleva un form para dicha accion donde puedes crear un curso y posterior mente ser redireccionado a esta vista de la tabla de la base de datos o al decidir no cancelar dicha accion te devuelve a la pantalla de bienvenida de la app.
 - Sedes, te renderiza una tabla de sedes registradas en la BD  asi como un boton para redireccionar a la creacion de nuevos usuarios. con una logica similar a las anteriores vistas.

3. La aplicacion cuenta con su gitignore asi como con su requirements.txt 
4. Se aplico herencia de templates
5. Cuenta con su entorno virtual
6. Se configuro la parte de /admin para poder tener superusuarios y visualizar mas comodamente desde django/admin el contenido de Users, de Course y de Branch.

