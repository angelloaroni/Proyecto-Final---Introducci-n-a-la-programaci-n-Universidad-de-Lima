# Proyecto-Final---Introducci-n-a-la-programaci-n-Universidad-de-Lima

Proyecto que usa los conceptos básicos de python (bucle for y while, manejo de tuplas, listas y diccionarios, funciones, etc), simulando un sistema de ventas de viajes
El enunciado trabajado es el siguiente:

Una empresa del rubro de turismo requiere un sistema que administre la venta de sus servicios:
1.	Los tipos de servicios: viajes nacionales, viajes internacionales y paquetes turísticos, información de los servicios: código de servicio (regla de generación es un aleatorio múltiplo de 5 entre 30000 y 80000), descripción, indicador si tiene beneficio tributario o no, precio sin IGV. 
2.	El precio sin IGV se calcula bajo la siguiente regla: viajes nacionales aleatorio par entre 150 y 350, viajes internacionales aleatorio múltiplo de 3 entre 380 Y 750, finalmente paquetes turísticos aleatorio impar entre 390 y 855.
3.	Se solicita la siguiente funcionalidad:
a.	Ingresar un servicio de cualquier tipo, calculando la información necesaria siguiendo las reglas anteriores.
b.	Registrar una venta, tener en cuenta los siguiente:
i.	El número de venta es un número correlativo comenzando en 1. 
ii.	El precio de venta el precio sin IGV más el 18% verifique si el servicio tiene beneficio tributario. 
iii.	Se puede tener cantidades mayores a 1 y menores a 10 (validarlo en el sistema), pero de un solo tipo de servicio.
iv.	Considerar el total de venta multiplicando la cantidad por el precio de venta. 
c.	Modificar la cantidad de una venta buscándola primero por número de venta, utilice la búsqueda binaria y como algoritmo de ordenamiento para utilizar la binaria, el algoritmo Quicksort. 
d.	Ordenar las ventas por total de venta utilizando el algoritmo burbuja. 
e.	Buscar una venta por el número de venta y mostrar todos sus datos utilizando la búsqueda secuencial.
f.	Mostrar la venta con el total de venta más alto.
g.	Almacenar toda la información en una localización física (archivo).
h.	Muestre las funcionalidades que se podrían realizar en el sistema como opciones de menú.
