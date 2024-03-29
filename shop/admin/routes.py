from flask import render_template, session, request, redirect, url_for, flash

from shop import app, db, bcrypt
from .forms import RegistrationForm, loginForm
from .models import User
from shop.products.models import Addproduct, Brand, Category
import os


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Please Login First','danger')
        return redirect(url_for('login'))
    
    products = Addproduct.query.all()
    return render_template('admin/index.html', title='Admin Page', products=products)

@app.route('/brands')
def brands():
    if 'email' not in session:
        flash(f'Please Login First','danger')
        return redirect(url_for('login'))
    
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='Brand Page', brands=brands)

@app.route('/categories')
def categories():
    if 'email' not in session:
        flash(f'Please Login First','danger')
        return redirect(url_for('login'))
    
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/brand.html', title='Categories Page', categories=categories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name = form.name.data, username = form.username.data, email = form.email.data,
                    password = hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.name.data} Thank you for registering','success')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Registrasi")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            if form.email.data == 'Admin@gmail.com':
                flash(f'Welcome {form.email.data}, You are logged in as admin', 'success')
                return redirect(url_for('admin'))
            else:
                flash(f'Welcome {form.email.data}, You are logged in', 'success')
                return redirect(url_for('beranda'))
        else:
            flash('Wrong Password, Please Try Again', 'danger')

    return render_template('admin/login.html', form=form, title='Masuk')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Clear the session data
        session.clear()
    # You may also want to do additional cleanup, such as revoking tokens or other actions
    
    # Redirect to the login page or another destination
        return redirect(url_for('login'))