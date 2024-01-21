from flask import Flask ,request,render_template
import requests
app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('index.html')

@app.route('/weatherapp',methods = ['GET','POST'])
def getweather_data():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q':request.form.get('city'),
        'appid':request.form.get('appid'),
        'units':request.form.get('units')
    }
    response = requests.get(url,params=param)
    data = response.json()
    return f'Data = {data}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')