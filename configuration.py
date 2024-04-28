URL_SERVICE = "https://eb955955-b6ed-4ca0-bf90-d76c70471f5f.serverhub.praktikum-services.ru"

DOC_PATH = "/docs/"
LOG_MAIN_PATH = "/var/www/backend/logs"
CREATE_ORDERS_PATH = "/api/v1/orders"
GET_ORDERS = "/api/v1/orders/track?t="

headers = {
    "Content-Type": "application/json"
}
order_body = {
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "address": "Valovaya, 4",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-04-30",
    "comment": "test-create orders",
    "color": [
        "BLACK"
    ]
}