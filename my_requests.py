# Импортируем необходимые библиотеки и модули
import requests
import configuration
import orders

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body,
                         headers=configuration.headers)
def get_orders(order_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS + str(order_id))