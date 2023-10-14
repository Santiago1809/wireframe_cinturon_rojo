import re
from flask import Blueprint, flash, redirect, render_template, request, session
from flask_app.model.User_Model import User
from flask_app.model.User_model_util import UserUtil
from werkzeug.security import generate_password_hash
user = Blueprint('user', __name__)

class UserController():
    @user.route('/', methods=['GET', 'POST'])
    def init():
        if request.method == 'POST':
            first_name = request.form['first_name']           
            last_name = request.form['last_name']
            email = request.form['email']
            password = request.form['password']
            c_password = request.form['c_password']
            if len(first_name) < 2 or len(last_name) < 2:
                flash('First Name and Last Name must be at least 2 characters')
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                flash("Email format is incorrect")
            if password != c_password:
                flash("Passwords doesn't match") 
            password = generate_password_hash(password)
            user = User(first_name, last_name, email, password, True)
            session['logged_in'] = True
            session['name'] = user.first_name + " " + user.last_name
            session['id'] = UserUtil().get_id(user.email)
            if user.find_user(user.email):
                flash("User already exists")
            result = user.save_user()
            print(result)
            if result == "Usuario guardado con éxito":
              return redirect('/thoughts')

        return render_template('index.html')
    
    @user.route('/login', methods=['POST'])
    def login():
        email = request.form['email_login']
        password = request.form['password_login']

        # Verifica si el usuario existe
        user = UserUtil().find_user_by_email(email)
        if user is None:
            flash("Usuario no existe")
            return redirect('/')

        # Verifica la contraseña
        if UserUtil().check_password(password, email):
            session['logged_in'] = True
            session['name'] = UserUtil().get_name(email)
            session['id'] = UserUtil().get_id(email)
            return redirect('/thoughts')
        else:
            flash("Contraseña incorrecta")
            return redirect('/')
        
    @user.route('/logout')
    def logout():
        session['logged_in'] = False
        return redirect('/')




