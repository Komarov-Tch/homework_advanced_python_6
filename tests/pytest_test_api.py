import pytest
from create_catalog_yandex import *

fixture_create_catalog = [
    ('new_catalog', 201),
    ('new_catalog_2', 201)
]


@pytest.mark.parametrize('catalog, code', fixture_create_catalog)
def test_create_catalog(catalog, code):
    result = create_catalog(catalog)
    assert code == result.status_code


@pytest.mark.xfail
def test_create_catalog_error():
    result = create_catalog('new_catalog_test')
    assert result.status_code == 201
