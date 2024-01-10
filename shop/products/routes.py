from flask import redirect, render_template, url_for, flash, request, session, current_app
from shop import db, app, photos
from .models import Brand, Category, Addproduct
from .forms import Addproducts
import secrets, os


@app.route('/')
def home():
    products = Addproduct.query.filter(Addproduct.stok > 0)
    barnds = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    categories = Category.query.join(Addproduct,(Category.id == Addproduct.category_id)).all()
    return render_template('products/index_before.html', products=products, barnds=barnds, categories=categories)

@app.route('/beranda')
def beranda():
    products = Addproduct.query.filter(Addproduct.stok > 0)
    barnds = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    categories = Category.query.join(Addproduct,(Category.id == Addproduct.category_id)).all()
    return render_template('products/index.html', products=products, barnds=barnds, categories=categories)

@app.route('/product/<int:id>')
def single_page(id):
    product = Addproduct.query.get_or_404(id)
    barnds = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    categories = Category.query.join(Addproduct,(Category.id == Addproduct.category_id)).all()
    return render_template('products/single_page.html', product=product,  barnds=barnds, categories=categories)


@app.route('/brand/<int:id>')
def get_brand(id):
    brand = Addproduct.query.filter_by(brand_id = id)
    barnds = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    categories = Category.query.join(Addproduct,(Category.id == Addproduct.category_id)).all()
    return render_template('products/index.html', brand=brand, barnds=barnds, categories=categories)

@app.route('/categories/<int:id>')
def get_category(id):
    get_cat_prod = Addproduct.query.filter_by(category_id=id)
    categories = Category.query.join(Addproduct,(Category.id == Addproduct.category_id)).all()
    barnds = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    return render_template('products/index.html', get_cat_prod=get_cat_prod, categories=categories, barnds=barnds)




@app.route('/addbrand', methods=['GET','POST'])
def addbrand():
    if 'email' not in session:
        flash(f'Please Login First','danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The Brand {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    
    return render_template('products/addBrand.html',brands='brands')

@app.route('/updatebrand/<int:id>', methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash(f'Please Login First','danger')
    
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == 'POST':
        updatebrand.name = brand
        flash(f'Your Brand has been updated','success')
        db.session.commit()
        return redirect(url_for('brands'))
    
    return render_template('products/updatebrand.html', title='Update Brand Page', updatebrand=updatebrand)

@app.route('/deletebrand/<int:id>', methods=['POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(brand)
        db.session.commit()
        flash(f'The Brand {brand.name} was deleted from your database','success')
        return redirect(url_for('admin'))
    
    flash(f'The Brand {brand.name} cant be deleted','warning')
    return redirect(url_for('admin'))

@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if 'email' not in session:
        flash(f'Please Login First','danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        getbrand = request.form.get('category')
        cat = Category(name=getbrand)
        db.session.add(cat)
        flash(f'The Category {getbrand} was added to your database','success')
        db.session.commit()
        return redirect(url_for('addcat'))
    
    return render_template('products/addBrand.html')

@app.route('/updatecat/<int:id>', methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash(f'Please Login First','danger')
    
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == 'POST':
        updatecat.name = category
        flash(f'Your Category has been updated','success')
        db.session.commit()
        return redirect(url_for('categories'))
    
    return render_template('products/updatebrand.html', title='Update Category Page', updatecat=updatecat)

@app.route('/deletecat/<int:id>', methods=['POST'])
def deletecat(id):
    category = Category.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(category)
        db.session.commit()
        flash(f'The Brand {category.name} was deleted from your database','success')
        return redirect(url_for('admin'))
    
    flash(f'The Brand {category.name} cant be deleted','warning')
    return redirect(url_for('admin'))

@app.route('/addproduct', methods=['POST','GET'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)

    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stok = form.stok.data
        colors = form.colors.data
        description = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + '.')
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + '.')
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + '.')

        addpro = Addproduct(name=name, price=price, discount=discount, stok=stok, colors=colors, description=description, brand_id=brand, category_id=category, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addpro)
        db.session.commit()
        flash(f'The Product {name} has been added to your databases','success')
        return redirect(url_for('admin'))

    return render_template('products/addproduct.html', title='Add Product', form=form, brands=brands, categories=categories)

@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    brands = Brand.query.all()
    categories = Category.query.all()
    product = Addproduct.query.get_or_404(id)

    brand = request.form.get('brand')
    category = request.form.get('category')

    form = Addproducts(request.form)

    if request.method =='POST':
        product.name = form.name.data
        product.price = form.price.data
        product.discount = form.discount.data
        product.stok = form.stok.data
        product.brand_id = brand
        product.category_id = category
        product.description = form.description.data
        product.colors = form.colors.data

        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images' + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + '.')
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + '.')

        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images' + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + '.')
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + '.')

        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images' + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + '.')
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + '.')


        db.session.commit()
        flash(f'Your Product has been updated','success')
        return redirect(url_for('admin'))

    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stok.data = product.stok
    form.description.data = product.description
    form.colors.data = product.colors


    return render_template('products/updateproduct.html', title='Update Product', form=form, brands=brands, categories=categories, product=product)

@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    product = Addproduct.query.get_or_404(id)
    if request.method == 'POST':
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, 'static/images' + product.image_1))
                os.unlink(os.path.join(current_app.root_path, 'static/images' + product.image_2))
                os.unlink(os.path.join(current_app.root_path, 'static/images' + product.image_3))
    
            except Exception as e:
                print(e)
        
        db.session.delete(product)
        db.session.commit()
        flash(f'The Product {product.name} was deleted from your database','success')
        return redirect(url_for('admin'))

    flash(f'Cant Delete the product','danger')
    return redirect(url_for('admin'))
