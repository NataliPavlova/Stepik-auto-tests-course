# Проверка ожидаемого результата
# Сообщение об ошибке с помощью исключения и конструкции try-except
def test_input_text(expected_result, actual_result):
    try:
        assert expected_result == actual_result
    except AssertionError:
        print(f'expected {expected_result}, got {actual_result}')