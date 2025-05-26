from flask import Flask, redirect, request, render_template
import secrets

app = Flask(__name__)
urls = {}  # Diccionario para almacenar URLs

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url_larga = request.form.get('url')
        clave = secrets.token_urlsafe(5)  # Ejemplo: "Abc12"
        urls[clave] = url_larga
        return f"URL acortada: http://tudominio.com/{clave}"
    return render_template('index.html')  # Plantilla HTML

@app.route('/<clave>')
def redirigir(clave):
    return redirect(urls.get(clave, "https://google.com"))  # Si no existe, redirige a Google

if __name__ == '__main__':
    app.run()