#!/bin/bash

# CFP20 - AMDELCO
# Laboratorio de Ciberseguridad

# Objetivo:
# Modificar una nota ficticia mediante HTTP POST.

echo "Modificando la nota del alumno..."

# -i muestra cabeceras y respuesta.
# -X POST indica el método HTTP.
# -H define el tipo de contenido JSON.
# -d envía los datos al servidor.

curl -i -X POST http://127.0.0.1:5000/api/nota \
  -H "Content-Type: application/json" \
  -d '{"nota": 10}'