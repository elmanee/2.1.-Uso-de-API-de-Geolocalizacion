from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        lugar = request.form['lugar']
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": lugar,
            "format": "json",
            "limit": 1
        }
        # El User-Agent es obligatorio para que la API no te rechace [cite: 43]
        headers = {"User-Agent": "Flask-Educational-App"}
        
        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            nombre = data[0]['display_name']
            return render_template('map.html', lat=lat, lon=lon, nombre=nombre)
        
        return render_template('map.html', error=True)
    
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)