import requests

new_catalog = 'new_catalog_test'


def create_catalog(catalog_name):
    token = 'Тут должен быть ваш токен яндекс'
    header = {'Content-Type': 'application/json',
              'Authorization': f'OAuth {token}'}
    url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + catalog_name
    response = requests.put(url=url, headers=header, timeout=5)
    return response


print(create_catalog(new_catalog))
