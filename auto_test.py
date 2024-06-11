# Зиялов Иван, 17-я когорта — Финальный проект. Инженер по тестированию плюс

import data
from sender_stand_request import create_order, get_order


# Автотест
def test_order_creation_and_retrieval():
    response = create_order(data.order_body)
    track_number = response.json()["track"]
    return get_order(track_number).status_code

    # Получение данных заказа по треку


def test_get_order_200():
    assert test_order_creation_and_retrieval() == data.status_code_200
