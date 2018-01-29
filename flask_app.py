from flask import  render_template
from manage import app, db, Product, ProductType, Spec


@app.route("/", methods=['GET'])
def index():
    products = Product.query.all()
    product_types = ProductType.query.all()
    return render_template('index.html',
                           products=products,
                           product_types=product_types)


@app.route("/product/<int:product_id>", methods=['GET'])
def product(product_id=None):
    product = Product.query.filter_by(id = product_id).first()
    return render_template('product.html', product=product)


@app.route("/bt", methods=['GET'])
def bt():
    return render_template('bt.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
