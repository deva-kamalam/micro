from flask import Flask, render_template,request,redirect
import requests
app=Flask(__name__)

@app.route("/")
def data():
    url_ab="http://127.0.0.1:5001/"
    response= requests.get(url_ab)
    data=response.json()
    return data

if __name__=="__main__":
    app.run(debug=True)