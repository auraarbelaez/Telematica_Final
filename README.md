# Proyecto_Final
# Aura Marcela Arbelaez Aristizabal
# Telematica 
# Id: 200236

¿Cual es el estado de los efluentes mas cercanos a mi ubicacion? 
Esto se llevara a cabo con los sensores de las estaciones de nivel de agua del SIATA.

# Pasos de creacion de la aplicacion web:
1. Crear un repositorio
2. Creamos los archivos propios de un proyecto
3. Creamos el Dockerfile para el login (DockerfileFront)
   - Utilizamos Flask para desarrollar la pagina de inicio de sesion y la autenticacion.
   - Utilizamos Dash para desarrollar las visualizaciones de los sensores de nivel de agua.
   - Implementamos la logica para consumir los datos de los sensores desde la URL proporcionada (http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/?format=json).
   - Desarrollamos la logica para generar las graficas de los niveles de agua.
   - Integramos la autenticacion para permitir el acceso solo a usuarios autorizados. (Estos datos de inicio de sesion quedaran guardados en la carpeta DB)
4. Construccion de la imagen Docker:
   - Abre una terminal y navega hasta el directorio del repositorio.
   - Ejecuta el comando para construir la imagen Docker utilizando el Dockerfile.
   - Verifica que la imagen se haya construido correctamente.
6. Despliegue del servicio en un servidor de produccion:
   - Utiliza un proveedor de servicios en la nube como AWS para desplegar tu servicio.
   - Configura una instancia de maquina virtual en AWS para ejecutar contenedores Docker.
   - Sube la imagen Docker al registro de contenedores de AWS.
   - Crea un cluster de contenedores en AWS.
   - Despliega y ejecuta la imagen Docker en el cluster.

# Pasos para desplegar la aplicacion
1. Creamos una maquina virtual
2. Clonamos el repositorio que creamos con todo el proyecto
3. Instalamos los programas necesarios para el despliegue de la aplicacion
4. Creamos un contenedor 
5. Corremos todos los archivos desde el contenedor utilizando docker


