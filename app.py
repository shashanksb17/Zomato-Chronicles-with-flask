# Import Flask
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)



# Main route
@app.route('/')
def index():
    return render_template('index.html')

# Menu route
@app.route('/menu')
def menu():
    return render_template('menu.html')

# Orders route
# Create an empty list to store the orders
orders = []

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        # Retrieve the form data
        customer_name = request.form['customer_name']
        dish_ids = request.form['dish_ids'].split(',')

        # Create a new order dictionary
        order = {
            'order_id': len(orders) + 1,
            'customer_name': customer_name,
            'dish_ids': dish_ids,
            'status': 'received'
        }

        # Add the new order to the orders list
        orders.append(order)
    elif request.method == 'GET' and 'order_id' in request.args:
        # Retrieve the order ID from the query parameters
        order_id = int(request.args['order_id'])
        status = request.args['status']

        # Update the status of the corresponding order
        for order in orders:
            if order['order_id'] == order_id:
                order['status'] = status
                break

    return render_template('orders.html', orders=orders)



# Run the application
if __name__ == '__main__':
    app.run()
