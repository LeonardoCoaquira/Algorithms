from flask import Flask, request, render_template

app = Flask(__name__)

def generar_tabla(filas, columnas):
    # Abrimos la etiqueta <table>
    tabla = "<table>"

    # Iteramos sobre cada fila y columna para agregar las celdas a la tabla
    for fila in range(filas):
        # Agregamos la etiqueta <tr> para cada fila
        tabla += "<tr>"
        for columna in range(columnas):
            # Agregamos la etiqueta <td> para cada columna
            tabla += "<td>A</td>"
        # Cerramos la etiqueta <tr> para cada fila
        tabla += "</tr>"

    # Cerramos la etiqueta </table>
    tabla += "</table>"

    # Retornamos la tabla generada
    return tabla

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/tabla')
def tabla():
    # Obtenemos los parámetros de filas y columnas desde la solicitud HTTP
    filas = int(request.args.get('filas', 3))
    columnas = int(request.args.get('columnas', 3))

    # Generamos la tabla HTML usando la función generar_tabla
    tabla_html = generar_tabla(filas, columnas)

    # Devolvemos la tabla generada como respuesta HTTP
    return tabla_html


if __name__ == '__main__':
    app.run(debug=True, port=8000)
