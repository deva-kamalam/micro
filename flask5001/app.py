from flask import Flask, render_template, request,redirect

app=Flask(__name__)
api_list=[]

@app.route("/")
def home():
    return api_list

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        name=request.form.get("name")
        age = request.form.get("age")
        mobile=request.form.get("mobile")
        details={
            "Name":name,
            "Age":age,
            "Mobile":mobile
        }
        api_list.append(details)
        return render_template("form.html",send=api_list)
    return render_template("form.html", send=api_list)

if __name__=="__main__":
    app.run(debug=True,port=5001)