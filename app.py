from flask import Flask, render_template, request, abort, make_response

app = Flask(__name__)
# Solo demostración: cambiar a True representa una corrección de permisos.
PROTEGIDO = False

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
    return render_template('notas.html', protegido=PROTEGIDO)

@app.route('/estado')
def estado():
    return {'aplicacion': 'Laboratorio CFP20', 'modo_protegido': PROTEGIDO, 'aviso': 'Datos ficticios'}

@app.errorhandler(403)
def prohibido(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def no_encontrado(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
