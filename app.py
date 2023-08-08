from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

from Infrastructure import Factory
from exceptions import NotFoundError, LimitQueriesError

app = Flask(__name__)

# MONGO_URI = os.environ.get("MONGO_URI", "mongodb://127.0.0.1:27017/samProject")

# create mongodb client
# app.config['MONGO_DBNAME'] = 'samProject'  # name of database on mongo
# app.config["MONGO_URI"] = "mongodb://mongo:27017/dev" #'mongodb://localhost:27017/samProject'
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config["MONGO_URI"] ="mongodb://mongo:27017/dev" #'mongodb://localhost:27017/samProject'#
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

mongo = PyMongo(app)
db_client = mongo.db
factory_instance = Factory(db_client)


@app.route('/')
def home_page():
    content = {
        'information about stock {IBM}': 'GET https://localhost:5000/stocks/{IBM}',
        'information about your total cost in $': 'GET http://localhost:5000/total-cost',
        'you can reset the total cost to 0': 'GET http://localhost:5000/total-cost/rest'
    }
    return jsonify({"content": content}), 200


@app.route('/stocks/<symbol_id>', methods=['GET'])
def get_stock(symbol_id):
    try:
        ip = request.remote_addr
        stock = factory_instance.stock_use_case.get_stock(symbol_id=symbol_id, ip=ip)
    except NotFoundError as e:
        return jsonify({"content": f"symbol id: {symbol_id} not exist"}), 404
    except LimitQueriesError as e:
        return jsonify({"content": f"{e}"}), 429
    except Exception as e:
        return jsonify({"content": f"server error: {e}"}), 500
    return jsonify(stock)


@app.route('/total-cost', methods=['GET'])
def get_total_cost():
    try:
        total_cost = factory_instance.total_cost_use_case.get_total_count()
    except Exception as e:
        return jsonify({"content": f"server error: {e}"}), 500
    return jsonify({'total_cost': total_cost})


@app.route('/total-cost/rest', methods=['POST'])
def reset_total_cost():
    try:
        factory_instance.total_cost_use_case.reset_total_count()
    except Exception as e:
        jsonify({"content": f"server error: {e}"}), 500
    return jsonify({})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
