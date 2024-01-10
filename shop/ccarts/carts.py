from flask import redirect, render_template, url_for, flash, request, session, current_app
from shop import db, app
from shop.products.models import Addproduct

@app.route('/addcart', methods=["POST"])
def AddCart():
    try:
        product_id= request.form.get('product_id')
        quantity= request.form.get('quantity')
        colors= request.form.get('colors')
        product= request.form.get('product')

        if product_id and quantity and colors and request.method =="POST":
            DicItems = {product_id: {'name': product.name, 'price': product.price, 'discount': product.discount, 'color': colors, 'quantity': quantity, 'image' : product.image_1}}

            if 'Shopcart' in session:
                print(session['ShoppingCart'])
            else:
                session['ShoppingCart'] = DicItems
                return redirect(request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)