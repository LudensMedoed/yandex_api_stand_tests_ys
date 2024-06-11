# Зиялов Иван, 17-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data


# Создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


# Получение заказа по номеру трекера
def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track_number),
                        headers=data.headers)
