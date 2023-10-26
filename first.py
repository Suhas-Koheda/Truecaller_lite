from flask import Flask,render_template,url_for,request
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import requests
url = "https://api.apilayer.com/number_verification/validate?number="
payload = {}
headers= {
  "apikey": "CSXdyBMEmGWItH9jfpfKv5meo8OmBeci"
}
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        number=request.form['number']
        response = requests.request("GET", url + number, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text
        x = result.split('{')
        x.remove(x[0])
        y = x[0].split('}')
        z = y[0].split('\n')
        z.remove(z[0])
        z.remove(z[10])
        y = ''
        for i in z:
            y = y + i
        u = y.split(',')
        for i in range(0, len(u)):
            u[i] = u[i].strip()
        return render_template ('result.html',valid=u[0],number=u[1],local=u[2],inter=u[3],pref=u[4],code=u[5],name=u[6],loc=u[7],carr=u[8],type=u[9],
)
    else:
        return render_template('index.html')
