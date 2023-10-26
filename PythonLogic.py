from flask import Flask,render_template,url_for,request
import requests

#api link!
url = "https://api.apilayer.com/number_verification/validate?number="
payload = {}
headers= {
  "apikey": "CSXdyBMEmGWItH9jfpfKv5meo8OmBeci"
}
#required Definition
l=[]
def simplify(i):
    x=u[i]
    y=x.split(':')
    y.remove(y[0])
    l.append(y[0].strip())
#Number request!
number=input('enter no:')
#Details request rom API!
response = requests.request("GET", url + number, headers=headers, data=payload)
#Status code!
status_code = response.status_code
#Splitting the result!
result = response.text
#Simplifying the result!
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
print(l)