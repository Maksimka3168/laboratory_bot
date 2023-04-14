import pyowm.commons.exceptions
from pyowm import OWM
from pyowm.utils.config import get_default_config


def get_weather(place: str):
    try:
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm = OWM('dd28aa6b6426ed4fdc8a7faa1d74f89c', config_dict)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        return observation.weather.temperature('celsius')
    except pyowm.commons.exceptions.NotFoundError:
        return {'error': 'Указанный город не найден'}
    except pyowm.commons.exceptions.InvalidSSLCertificateError:
        return {'error': 'Превышено максимальное кол-во запросов, попробуйте через минуту.'}



