👥 PRODUCT OWNER

Problema que resuelve 
Se solucionará la problemática de desinformación en los turistas en ubicaciones desconocidas sobre la gastronomía local. 

Solución
Se desarrollará una aplicación llamada SNACKMAP, la cual permitirá a los turistas acceder a un mapa con los restaurantes de las diferentes ciudades que visiten, brindándoles información como precios exactos y actualizados del menú, información sobre la estructura y el ambiente del restaurante, entre otras, dependiendo de los filtros o preferencias que aplique el usuario. 

Público objetivo

Turistas 

3 features 

• Registro de restaurante con características y precios 

• ⁠Registro de usuario con preferencias 

• ⁠Validación de ubicación y/o elección de localidad.


🎨 Diseñador UX/UI - Bocetos y flujo


Vista de adición de restaurantes: 


![vistaRestaurante](https://github.com/user-attachments/assets/bab2eb12-2e60-42e8-97e0-10c6fbe1f535)

Vista busqueda de restaurantes:


![vistaUsuario](https://github.com/user-attachments/assets/7af0234b-9498-4372-8081-b9da77b197e3)


🛠️ Desarrollador - Implementación

•	Feature implementada:  Registro de restaurante con características y precios


🔧 QA Tester - Pruebas
Caso de prueba 1: Registro exitoso de restaurante nuevo

•	Objetivo: Confirmar que se pueda registrar un restaurante nuevo con datos válidos sin inconvenientes.

•	Errores potenciales:
1.	Que el restaurante no se guarde en el rango adecuado.
  
2.	Que el archivo no se genere si no existe previamente.
   
3.	Que los datos no se graben correctamente.
   
Caso de prueba 2: Prevención de duplicados

•	Objetivo: Asegurarse de que no se permita registrar un restaurante con el mismo nombre que ya existe.

•	Errores potenciales:
1.	Permitir el registro duplicado si se usan variaciones en mayúsculas o espacios.
2.	Fallos en la comparación del nombre por no utilizar .lower() para validar.
Caso de prueba 3: Consulta por categoría
•	Objetivo: Verificar que al seleccionar una categoría, se muestren todos los restaurantes correspondientes.
•	Errores potenciales:
1.	Que el input no sea validado correctamente.
2.	Que no se muestren resultados aunque existan datos en el archivo.
3.	Que ocurran errores al acceder al archivo JSON si está dañado.
