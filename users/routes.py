from users import app
from flask import render_template,redirect,url_for,flash,request
from users.models import db
from users.models import User
from users.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required
import pickle
from users.data import lrg 
import numpy as np

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create=User(name=form.name.data,email=form.email.data,password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.name}", category='success')
        return redirect(url_for("profile_page"))

    if form.errors!={}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email=form.email.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in with: {attempted_user.email}', category='success')
            return redirect(url_for("profile_page"))
        else:
            flash('Username and password do not match! Please try again', category='danger')

    return render_template('login.html',form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))

@app.route('/profile',methods=['GET','POST'])
def profile_page():
    return render_template('profile.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/blogs')
def blogs_page():
    return render_template('blogs.html')

@app.route('/cancer_result',methods=['GET','POST'])
def cancer_result_page():
    return render_template('cancer_result.html')

@app.route('/stroke_result',methods=['GET','POST'])
def stroke_result_page():
    return render_template('stroke_result.html')

@app.route('/stroke',methods=['GET','POST'])
def stroke_page():
    return render_template('stroke.html')

@app.route('/stroke_predict',methods=['GET','POST'])
def stroke_predict():
    model=pickle.load(open('data.pkl','rb'))
    data1 = int(request.form["q22_gender"]) 
    data2 = int(request.form["q21_age"])
    data3 = int(request.form["q23_doYou"])
    data4 = int(request.form["q24_doYou24"])
    data5 = int(request.form["q25_haveYou"])
    data6 = int(request.form["q26_whatIs"])
    data7 = int(request.form["q27_whatIs27"])
    data8 = float(request.form["q28_whatIs28"])
    data9 = float(request.form["q29_whatIs29"])
    data10 = int(request.form["q30_whatIs30"])
    arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]])
    pred = model.predict(arr)
    return render_template('stroke_result.html', data=pred)

@app.route('/strokeBlog',methods=['GET','POST'])
def stroke_blog_page():
    return render_template('strokeblog.html')

@app.route('/cancer',methods=['GET','POST'])
def cancer_page():
    return render_template('cancer.html')

@app.route('/cancerBlog',methods=['GET','POST'])
def cancer_blog_page():
    return render_template('cancerblog.html')

@app.route('/cancer_predict',methods=['GET','POST'])
def cancer_predict():
    model1=pickle.load(open('dataCan.pkl','rb'))
    data1 = int(request.form["q10_gender"]) 
    data2 = int(request.form["q26_age"])
    data3 = int(request.form["q27_enterLevel"])
    data4 = int(request.form["q28_enterYour"])
    data5 = int(request.form["q29_enterYour29"])
    data6 = int(request.form["q30_enterYour30"])
    data7 = int(request.form["q31_enterYour31"])
    data8 = int(request.form["q32_enterYour32"])
    data9 = int(request.form["q33_enterYour33"])
    data10 = int(request.form["q45_enterYour45"])
    data11 = int(request.form["q46_enterYour46"]) 
    data12 = int(request.form["q47_enterYour47"])
    data13 = int(request.form["q34_enterYour34"])
    data14 = int(request.form["q35_enterYour35"])
    data15 = int(request.form["q36_enterYour36"])
    data16 = int(request.form["q37_enterYour37"])
    data17 = int(request.form["q38_enterYour38"])
    data18 = int(request.form["q39_enterYour39"])
    data19 = int(request.form["q40_enterYour40"])
    data20 = int(request.form["q41_enterYour41"])
    data21 = int(request.form["q42_enterYour42"])
    data22 = int(request.form["q43_enterYour43"])
    data23 = int(request.form["q44_enterYour44"])
    arr1 = np.array([[data2,data1,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23]])
    pred = model1.predict(arr1)
    return render_template('cancer_result.html', data=pred)
