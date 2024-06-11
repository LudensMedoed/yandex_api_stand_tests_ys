# Вывод списка логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).

 SELECT c.login, COUNT(o.id) AS "deliveryCount"
   FROM "Couriers" AS c
   LEFT JOIN "Orders" AS o ON c.id = o."courierId"
   WHERE o."inDelivery" = true
   GROUP BY c.login;


# Вывод всех трекеров заказов и их статусов. Статусы определяются по следующему правилу:
# Если поле finished == true, то вывести статус 2.
# Если поле canсelled == true, то вывести статус -1.
# Если поле inDelivery == true, то вывести статус 1.
# Для остальных случаев вывести 0

SELECT track,
          CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
  ELSE 0 END AS status
    FROM "Orders";