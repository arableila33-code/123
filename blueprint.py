from flask import Blueprint, render_template

products_bp = Blueprint(
    "products", __name__, url_prefix="/products", template_folder="/products"
)


@app.route("/<id:int>")
def get(id: int):
    products = (
        get_random_products()
    )  # exercise 2.2. Return hard coded list if you have not done it
    # No database call is needed. Fetch the id from the list with index.
    # You need error handling if the id does not exist in the list
    product = products[id]
    return render_template("template.html", product=product)
