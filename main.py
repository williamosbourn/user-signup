from flask import Flask, request, redirect, render_template 
import html
import os

app = Flask(__name__)
app.config['DEBUG'] = True 

@app.route("/")
def index():
  return render_template('signup.html') 




@app.route("/signup", methods= ['POST'])
def signup():
  username = request.form['username']
  password = request.form['password']
  verify_password = request.form['verify_password']
  email = request.form['email']

  # if (not new_movie) or (new_movie.strip() == ""):
  #   error = "Please specify the movie you want to add."
  #   return redirect("/?error=" + error)  




app.run()