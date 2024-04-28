#Анна Акмаева, 15-я когорта, финальный проект инженер по тестированию плюс
import my_requests
import configuration

def test_order_response_status():
    # Assuming orders.order_body is defined and valid
    track = my_requests.post_new_order(configuration.order_body).json().get('track')
    order = my_requests.get_orders(track)
    assert order.status_code == 200