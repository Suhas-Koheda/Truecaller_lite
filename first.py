from flask import Flask,render_template,url_for,request
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        number=request.form['number']
        phoneNumber = phonenumbers.parse(number)
        if(phonenumbers.is_valid_number(phoneNumber)):
            yourLocation = geocoder.description_for_number(phoneNumber,"en")
            yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
            t_zone=timezone.time_zones_for_geographical_number(phoneNumber)
            if(yourLocation=="India" and yourServiceProvider=="Telewings"):
                yourServiceProvider="Airtel"
            else:
                yourServiceProvider=yourServiceProvider
        return render_template('result.html',yourLocation=yourLocation,yourServiceProvider=yourServiceProvider,t_zone=t_zone)
    else:
        return render_template('index.html')