# PythonApp- Adei Dsoo Cabañas González
0. Video
[![Video PythonApp-Pizza](/media/image/Pythonapp-Pizzas.png)](https://www.loom.com/embed/1c9ec2c9231d4cdab1d88cace0c11f9c?sid=0c2437de-c328-48bf-a7c5-b1c1f7ef73ef)

1. Inicia con una pantalla de bienvenida con un navbar con 5 botones; del lado izquierdo esta el boton de inicio que te regresa al home.
2. del lado derecho estan, en orden de aparecion de derecha a izquierda, boton about me, pizzas, iniciar sesión y registrarse.
3. el boton about me es un template simple que solo cumple el requisito de renderizar una vista con informacion estatica 'sobre mi'
4. pizzas, nos lleva a toda la navegacion relacionada con el CRUD de las mismas. Partiendo de una vista donde se enlistan las pizzas creadas o en sud efecto un mensaje de no hay pizzas creadas aun. en esta vista solo se puede acceder a ver detalle sin estar logeado. todas las demas acciones como crear, eliminar editar se requiere loguearse. Asi mismo tambien las pizzas pueden tener una imagen que les acompañe si asi se desea.
5. Iniciar sesion. es un boton donde te solicita tu username y contraseña para ingresar al loguearte si es que tienes un avatar asociado a tu perfil se rederizara a lado de tu nombre, en el navbar. y podras acceder a las funciones completas del CRUD de pizzas. 
Al darle click a eliminar una pizza te pide doble comprobacion de si estas seguro que deseas eliminarla. al editar  puedes ver la imagen asociada al perfil al darle clic al vinculo, etc.
6. Asi mismo cuando te logueas el boton de registrarse desaparece y aparecen dos nuevos botones que son: perfil y cerrar sesion. Perfil te permite ahondar en otros elementos del mismo como hobbies firstname, lastname, email, etc. avatar etc si asi se desea y mantener actualizado el perfil del usuario. 
7. tambien es importante recalcar que el nombre mismo del usuario que aparece en el navbar se vuelve un boton donde al hacer clic te permite visualizar los datos del perfil del usuario. 
8. por ultimo al cerrar sesion se mostrara un aviso de se ha cerrado sesion correctamente. 
9. Lo que nos lleva al punto que nos falta explicar que es el de usuarios que no se han registrado anteriormente en la aplicacion. Dichos usuarios van al boton de registrarse se le solicitan ciertos datos se registran y posteriormente se les redirecciona a la pantalla de login ingresan y tienen acceso a todas funcionalidades anteriormente descritas. 
