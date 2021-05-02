from flask import Flask, jsonify, request
from Lista.Lista import ListaEnlazada

listadatos = ListaEnlazada()
app = Flask(__name__)

@app.route('/ping')
def ping():
    return "algo"

@app.route('/setInformacion',methods=['POST'])
def setInformacion():
    datos = request.get_json()
    for info in datos:
        fecha = info['fecha']
        usuario = info['usuario']
        afectado = info['afectado']
        codigo = info['codigo']
        error = info['error']
        listadatos.incertar(fecha,usuario,afectado,codigo,error)

    print("Agregados correctamente")
    return jsonify({"mensage":"Informacion aceptada correctamente"})

@app.route('/getInformacion',methods=['GET'])
def getInformacion():
    datos = listadatos.retornarInfomacion()
    return jsonify(datos)

@app.route('/search/<string:dato1>/<string:dato2>')
def search(dato1,dato2):
    datos = listadatos.busqueda(dato1,dato2)
    print("dato1: "+dato1+" dato2: "+dato2)
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)