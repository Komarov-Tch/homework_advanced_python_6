import pytest
import mock
import builtins
from app import *

fixture_check_document = [
    ('11-2', True),
    ('10-4', False),
    ('', False)
]

fixture_doc_remove = [
    ('11-2', True),
    ('10-4', None),
    ('', None)
]

fixture_shelf_number = [
    ('4', ('4', True)),
    ('1', ('1', False))
]

fixture_append_doc_to_shelf = [
    ('1', '234', True),
    ('3', '13-2', True),
    ('5', '12345', True)
]

fixture_delete_doc = [
    ('11-2', ('11-2', True)),
    ('12345', None)
]

fixture_get_doc_shelf = [
    ('11-2', '1'),
    ('12345', None)
]
fixture_move_doc_to_shelf = [
    ('11-2', '1', True),
    ('12312', '7', True)
]

fixture_doc_info = [
    ({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}, 'passport "2207 876234" "Василий Гупкин"')
]

fixture_show_all_docs_info = [
    (['passport "2207 876234" "Василий Гупкин"',
      'invoice "11-2" "Геннадий Покемонов"',
      'insurance "10006" "Аристарх Павлов"'])
]

fixture_add_new_doc = [
    ('1234', 'pasport', 'Петр Иванович', '3', '3'),
    ('123-111', 'transport number', 'Сергей Михайлович', '6', '6')
]


@pytest.mark.parametrize('doc, res', fixture_check_document)
def test_check_document_existance(doc, res):
    result = check_document_existance(doc)
    assert result is res


def test_get_all_doc_owners_names():
    result = get_all_doc_owners_names()
    assert result == {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}


def test_get_doc_owner_name():
    with mock.patch.object(builtins, 'input', lambda _: '11-2'):
        assert get_doc_owner_name() == 'Геннадий Покемонов'


@pytest.mark.parametrize('doc_num, res', fixture_doc_remove)
def test_remove_doc_from_shelf(doc_num, res):
    result = remove_doc_from_shelf(doc_num)
    assert result is res


@pytest.mark.parametrize('shelf_number, res', fixture_shelf_number)
def test_add_new_shelf(shelf_number, res):
    result = add_new_shelf(shelf_number)
    assert result == res


@pytest.mark.parametrize('doc, shelf, res', fixture_append_doc_to_shelf)
def test_append_doc_to_shelf(doc, shelf, res):
    result = append_doc_to_shelf(doc, shelf)
    assert result is res


@pytest.mark.parametrize('doc_num, res', fixture_delete_doc)
def test_delete_doc(doc_num, res):
    result = delete_doc(doc_num)
    assert result == res


@pytest.mark.parametrize('doc, res', fixture_get_doc_shelf)
def test_get_doc_shelf(doc, res):
    result = get_doc_shelf(doc)
    assert result == res


@pytest.mark.parametrize('doc, shelf, res', fixture_move_doc_to_shelf)
def test_move_doc_to_shelf(doc, shelf, res):
    result = move_doc_to_shelf(doc, shelf)
    assert result == res


@pytest.mark.parametrize('document, res', fixture_doc_info)
def test_show_document_info(document, res):
    result = show_document_info(document)
    assert res == result


@pytest.mark.parametrize('res', fixture_show_all_docs_info)
def test_show_all_docs_info(res):
    result = show_all_docs_info()
    assert result == res


@pytest.mark.parametrize('new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, res',
                         fixture_add_new_doc)
def test_add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, res):
    result = add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number)
    assert result == res
