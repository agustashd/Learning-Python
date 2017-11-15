# Farmasoft

## Flujo del programa
El programa da la bienvenida, y pide al usuario que ingrese o se registre en el sistema. Una vez ingresado se le presentan varias secciones donde se puede consultar las ultimas ventas,  otro tipo de consultas sobre los clientes y los productos y finalmente descargar los resultados de las tablas en formato CSV

## Estructura de los archivos
Se utiliza el lenguaje Python en su version 3.6 para el archivo principal, el modulo forms y el modulo data_manipulation. Para las bases de datos de los usuarios y la farmacia se utilizan archivos .csv y se manipulan con los modulos Pandas y CSV, para mostrar los resultados obtenidos de estos archivos se emplearon tablas.

## Uso del programa
El usuario debera registrarse mediante el boton "Registrarse" o ingresar con su cuenta con el boton de "Login", ambos ubicados en la esquina superior derecha de la pantalla. Una vez ingresado, el usuario es bienvenido y se le habilitan las funciones centrales del programa.

- Inicio: bienvenida al usuario acompañada de un link a la pantalla para hacer Logout.
- Ultimas ventas: tabla con las ultimas 5 ventas realizadas.
- Consultas:
  - Productos por cliente: se selecciona un cliente de la lista y se devuelven todas los productos comprados por el mismo.
  - Clientes por producto: se selecciona un producto de la lista y se devuelven todas los clientes que compraron dicho producto.
  - Productos mas vendidos: se muestra una lista con los 5 productos mas vendidos.
  - Mejores clientes: se muestra una lista con los 5 clientes que mas compraron.
- Logout: se cierra la sesion y redirecciona a la pantalla de login.

 Todas las tablas mostradas en el programa pueden ser descargadas en formato CSV mediante un link que se encuentra arriba de ellas.
 Antes de mostrar las vistas se corrobora el estado de la base de datos y se informa al usuario si se encuentran errores.

## Clases diseñadas
Se diseñaron 3 clases de formularios ya que tenian distintos campos y funciones.
* LogForm para la parte del ingreso del usuario
* RegForm para la parte de registro del usuario
* QueryForm para la parte de consultas donde se selecciona de una lista ya sea de clientes o productos
