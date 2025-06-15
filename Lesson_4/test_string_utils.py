import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("Марфа", "Марфа"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected





@pytest.mark.positive
@pytest.mark.parametrize("string, expected", [
       (" skypro", "skypro"),
       ("  Python программа", "Python программа"),
       ("   ", ""),

       ])
def test_positive_trim(string, expected):
    string_utils = StringUtils()
    assert string_utils.trim(string) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, expected", [
    ("sky","sky"),
    ("", ""),
    None
    ])
def test_negative_trim(string, expected):
    string_utils = StringUtils()
    assert string_utils.trim(string) == expected





@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, result", [
      ("skypro", "y", True),
      ("sky pro", "Z", False),
      ("Дом", "м", True),
      ("Солнце", "G", False),
      ("Home1", "1", True)
      ])
def test_positive_contains(string, symbol, result):
    string_utils = StringUtils()
    assert string_utils.contains(string,symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, result", [
      (" ", "A", False),
      ("", "", False)
       ])
def test_negative_contains(string, symbol, result):
    string_utils = StringUtils()
    assert string_utils.contains(string, symbol) == result





@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, result", [
    ("sky pro", "pro", "sky"),
    ("Люблю грозу в начале", "в", "Люблю грозу  начале"),
    ("Иван 3", "3", "Иван"),
    ("Победа!", "!", "Победа"),
    ("12345", "13", "245")
    ])
def test_positive_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(string, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, result", [
    ("Люблю грозу в начале", "", "Люблю грозу в начале"),
    ("", "A", ""),
    ("skypro", "m", "skypro")
    ])
def test_negative_delete_symbol(string, symbol, result):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(string, symbol) == result
