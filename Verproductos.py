# app.py
from flask import Flask, request, render_template_string
import openpyxl

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        producto = request.form['producto']
        cantidad = request.form['cantidad']
        precio = request.form['precio']

        wb = openpyxl.load_workbook('registro_productos.xlsx')
        ws = wb.active
        ws.append([producto, cantidad, precio])
        wb.save('registro_productos.xlsx')

        return 'Producto registrado correctamente.'

    return render_template_string('''
        <form method="post">
            Producto: <input name="producto"><br>
            Cantidad: <input name="cantidad"><br>
            Precio: <input name="precio"><br>
            <button type="submit">Registrar</button>
        </form>
    ''')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

