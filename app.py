from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

# Просто черный экран с картинкой по центру
HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #000;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        img {
            max-width: 100%;
            max-height: 100%;
        }
    </style>
</head>
<body>
    <img src="/image">
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/image')
def image():
    # Отдаем картинку
    return send_from_directory('.', 'demon.jpg')

if __name__ == '__main__':
    # Ботош сам подставит нужный порт
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
