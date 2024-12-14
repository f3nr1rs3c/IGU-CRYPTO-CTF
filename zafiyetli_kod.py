import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Dosya Kontrol Sistemi</h1>
    <p>'dosya' adındaki dosyanın içeriğini kontrol etmek için bir uzantı girin. Örnek: /check?ext=txt</p>
    """

@app.route('/check')
def check_file():
    file_extension = request.args.get('ext')
    if not file_extension:
        return "Dosya uzantısı belirtilmedi!", 400

    command = f"cat dosya.{file_extension}"
    try:
        output = os.popen(command).read()
        return f"<pre>{output}</pre>"
    except Exception as e:
        return f"Hata: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
