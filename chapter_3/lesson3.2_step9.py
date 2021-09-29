# Cоставные сообщения об ошибках и поиск подстроки

def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
    # Для автоматической подстановки кавычек можно ставить !r после переменной.
    # assert substring in full_string, f"expected {substring!r} to be substring of {full_string!r}"

test_substring('fulltext', 'some_value')
