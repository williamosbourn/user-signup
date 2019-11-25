from flask import Flask, request, redirect, render_template, escape
import html
import os
import re

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
  email_error = ''

  if (not user_name) or (user_name.strip() == "") or len(user_name) < 3 or len(user_name) > 20:
    username_error = "That's not a valid username"
    user_name = ''
  if (not password) or (password.strip() == ""):
    password_error = "That's not a valid password"
    password = ''
  if (not verify_password) or (verify_password.strip() == ""):
    v_password_error = "That's not a valid password"
    verify_password = ''
  if verify_password != password:
    v_password_error = "Passwords do not match"
    verify_password = ''
  
  if len(e_mail) > 0:
    if "@" not in e_mail or '.' not in e_mail or ' ' in e_mail:
      email_error = "That's not a valid email"
      e_mail = ''
    else:
      if len(e_mail) < 3 or len(e_mail) > 20:
        email_error = "That's not a valid email"
        e_mail = ''

  
  
  if not username_error and not password_error and not v_password_error and not email_error:
    username = request.form['u_name']
    return render_template('welcome.html', username=username) 
  
  return render_template('home.html', u_error=username_error, p_error=password_error, username=user_name, p_word=password, v_pass_error=v_password_error, email_error=email_error, email=e_mail) 


@app.route("/welcome", methods=['POST'])
def welcome():
  username = request.form['u_name']
  return render_template('welcome.html', username=username) 


app.run()