from flask import Flask, render_template, request, abort, make_response, jsonify

app = Flask(__name__)
# Solo demostración: cambiar a True representa una corrección de permisos.
PROTEGIDO = False

alumno = {
    "nombre": "Juan",
    "nota": 7
}

@app.after_request
def headers(respuesta):
    respuesta.headers['Cache-Control'] = 'no-store'
    respuesta.headers['X-Content-Type-Options'] = 'nosniff'
    return respuesta

@app.route('/')
def inicio():
    return render_template('inicio.html', protegido=PROTEGIDO)

@app.route('/notas')
def notas():
    # Simulamos una persona no autenticada. Nunca usar datos reales.
    if PROTEGIDO:
        abort(403)
    return render_template(
    'notas.html',
    protegido=PROTEGIDO,
    alumno=alumno
)

@app.route('/estado')
def estado():
    return {'aplicacion': 'Laboratorio CFP20', 'modo_protegido': PROTEGIDO, 'aviso': 'Datos ficticios'}

@app.errorhandler(403)
def prohibido(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def no_encontrado(error):
    return render_template('404.html'), 404


# Consultar la nota almacenada en el servidor
@app.route('/api/nota', methods=['GET'])
def consultar_nota():
    return jsonify(alumno)


# Modificar la nota mediante una solicitud POST
@app.route('/api/nota', methods=['POST'])
def cambiar_nota():
    # En modo protegido, bloqueamos las modificaciones
    # Esta es una simulación didáctica, no autenticación real.
    if PROTEGIDO:
        return jsonify({"error": "Acceso denegado"}), 403

    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({"error": "Se requiere JSON"}), 400

    nueva_nota = datos.get("nota")

    # Validamos que sea un entero entre 0 y 10
    if type(nueva_nota) is not int or not 0 <= nueva_nota <= 10:
        return jsonify({"error": "Nota inválida"}), 400

    # Vulnerabilidad intencional:
    # no comprobamos la identidad del usuario.
    alumno["nota"] = nueva_nota

    return jsonify({
        "mensaje": "Nota modificada correctamente",
        "alumno": alumno
    })



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)



