from flask import Flask, request, redirect, render_template, escape
import html
import os

app = Flask(__name__)
app.config['DEBUG'] = True 

@app.route("/")
def index():
  return render_template('home.html') 


@app.route("/", methods= ['GET', 'POST'])
def signup():
  user_name = request.form['u_name']
  password = request.form['p_word']
  verify_password = request.form['verify']
  e_mail = request.form['emailaddress']

  username_error = ''
  password_error = ''
  v_password_error = ''

  if (not user_name) or (user_name.strip() == "") or len(user_name) < 3 or len(user_name) > 20:
    username_error = "That's not a valid username"
    user_name = ''
  if (not password) or (password.strip() == ""):
    password_error = "That's not a valid password"
    password = ''
  if (not verify_password) or (verify_password.strip() == ""):
    v_password_error = "That's not a valid password"
    verify_password = ''
  
  
  


  
  return render_template('home.html', u_error=username_error, p_error=password_error, username=user_name, p_word=password, v_pass_error=v_password_error, email=e_mail)


    




app.run()