#all imports!
from flask import Flask,render_template,url_for,request
<<<<<<< HEAD
import requests

#api link!
=======
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import requests
>>>>>>> 5849315fb085c64867b3c9053b554a16219d609f
url = "https://api.apilayer.com/number_verification/validate?number="
payload = {}
headers= {
  "apikey": "CSXdyBMEmGWItH9jfpfKv5meo8OmBeci"
}
<<<<<<< HEAD
#Flask definition!
=======
>>>>>>> 5849315fb085c64867b3c9053b554a16219d609f
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        #Number request!
        number=request.form['number']
<<<<<<< HEAD
        #Details request rom API!
        response = requests.request("GET", url + number, headers=headers, data=payload)
        #Status code!
        status_code = response.status_code
        #Splitting the result!
        result = response.text
        #Simplifying the result!
=======
        response = requests.request("GET", url + number, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text
>>>>>>> 5849315fb085c64867b3c9053b554a16219d609f
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
<<<<<<< HEAD
        #Choosing the required details!
        #required Definition
        l=[]
        def simplify(i):
            x=u[i]
            y=x.split(':')
            y.remove(y[0])
            l.append(y[0].strip())
        simplify(0)
        simplify(1)
        simplify(2)
        simplify(3)
        simplify(4)
        simplify(5)
        simplify(6)
        simplify(7)
        simplify(8)
        simplify(9)
        #Returning the result!
        if(l[0]=='true'):
            return render_template ('result.html',inter=l[3],pref=l[4],code=l[5],name=l[6],loc=l[7],carr=l[8],type=l[9])
        else:
            return render_template('error.html')
=======
        return render_template ('result.html',valid=u[0],number=u[1],local=u[2],inter=u[3],pref=u[4],code=u[5],name=u[6],loc=u[7],carr=u[8],type=u[9],
)
>>>>>>> 5849315fb085c64867b3c9053b554a16219d609f
    else:
        return render_template('index.html')
