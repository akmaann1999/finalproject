--Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 
SELECT Couriers.login, COUNT(Orders.inDelivery) AS inDeliveryCount
FROM "Couriers"
INNER JOIN "Orders" ON Couriers.id = Orders.courierId
WHERE Orders.inDelivery = true
GROUP BY Couriers.id, Couriers.login;


--Статусы определяются по следующему правилу:
--Если поле finished == true, то вывести статус 2.
--Если поле canсelled == true, то вывести статус -1.
--Если поле inDelivery == true, то вывести статус 1.
--Для остальных случаев вывести 0.
SELECT order_track,
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN inDelivery = true THEN 1
           ELSE 0
       END AS order_status
FROM "Orders";