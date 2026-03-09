from enum import Enum


class AppRoute(str, Enum):
    CREATE_COURIER = "/api/v1/courier"
    DELETE_COURIER = "/api/v1/courier/"
    LOGIN_COURIER = "/api/v1/courier/login"
    CREATE_ORDER = "/api/v1/orders"
    GET_ORDER = "/api/v1/orders"
