import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# @pytest.fixture
# def string_utils():
#     return StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),# корректное преобразование первой буквы в заглавную
    ("hello world", "Hello world"), # корректное преобразование первой буквы в заглавную с пробелами
    ("Марфа", "Марфа"),# корректное преобразование первой буквы в заглавную на кириллице
    ("python5.1", "Python5.1"), # корректное преобразование первой буквы в заглавную с цифрами
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"), # Проверка строки, начинающейся с цифр
    ("", ""),# Проверка пустой строки
    ("   ", "   "),# Проверка строки, только из пробелов
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
       (" skypro", "skypro"),# Проверка удаления одного пробела в начале строки
       ("  Python программа", "Python программа"),# Проверка удаления нескольких пробелов в начале строки с пробелами внутри строки
])
def test_positive_trim(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("sky","sky"),# Проверка строки без пробелов
    ("   ", ""),# Проверка строки, состоящей только из пробелов
    ("", "")# Проверка пустой строки
])
def test_negative_trim(input_str, expected):
    assert string_utils.trim(input_str) == expected



@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
      ("skypro", "s", True), # Проверка наличия символа в начале строки
      ("sky pro", "y", True), # Проверка наличия символа в середине строки
      ("Дом", "м", True), # Проверка наличия символа в конце строки
      ("Home123", "1", True), # Проверка наличия символа в строке состоящей из цифр
])
def test_positive_contains(input_str, symbol, expected):
    assert string_utils.contains(input_str,symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
      ("Grinch", "A", False), # Проверка отсутствия символа в строке
      ("", "", False), # Проверка пустой строке
       ])
def test_negative_contains(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected



@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("sky pro", "pro", "sky"),# Проверка удаления символов из строки
    ("Люблю грозу в начале", "в", "Люблю грозу  начале"),# Проверка удаления символа из строки
    ("Иван 3", "3", "Иван"),# Проверка удаления цифры из строки
    ("Победа!", "!", "Победа"), # Проверка удаления символа из строки
    ("12345", "13", "245"), # Проверка удаления цифры из строки с цифрами
    ])
def test_positive_delete_symbol(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Люблю грозу в начале", "", "Люблю грозу в начале"),# Проверка удаления пустого символа из строки
    ("", "A", ""),# Проверка удаления символа из пустой строки
    ("skypro", "m", "skypro")# Проверка удаления отсутствующего символа из строки
    ])
def test_negative_delete_symbol(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected