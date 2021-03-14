# TODO:
- 

# walmart

Lo que se me ocurre que puede ser es:
un endpoint para clientes que tengan datos, en donde puedan subir sus propios datos y calcular el riesgo priorisando sus
datos

me precupa que si no priorisamos sus datos los valores para sus alarmas van a ser muy bajos o muy similares

## propuestas

- opcion 1: hacer nuevo endpoint en el api, seria un endpoint que en mascare el anterior para no perder la anterior
  funcionalidad
- opcion 2: modifical calculo de riesgo actual y consevar solo el nuevo

## Nueva formaula

```
Riesgo = Formato (.35) + Origen (.2) + Ruta (0.3) + Línea transportista (.15)
```

## necesitamos

- limpiar datos
- normalizar datos
- subir datos
- endpoint para subir datos / admin de django
- calcular riesgos (4)
- crear modelos
- implementar nuevo caculo de riesgo
- vista del api

## datos de riesgo nuevos para el modelo

- Formato: riesgo del (sam's, supercenter, superama, bodega)
- Origen: riesgo del lugar de origen
- Ruta: riesgo de la ruta
- linea de transportistas: riesgo de la linea de transportistas

## datos

- información recabada por protección de activos
- catalogo de _Formato_, _Linea de transportistas_, _origenes_
- cordenadas de origenes

## variables walmart

- Formato (35%)
- Origen (20%)
- Ruta (30%)
- Línea Transportista (15%)

## walmart recursos confiables

walmar recursos confiables 10 mil viajes diarios

15 mil unidad

sesiones martes y jueves con walmart

# para actualizar formula

- dag que popule las categorias
-
