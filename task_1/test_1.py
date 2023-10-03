from api_utils import check_text


def test_step1(valid_text, invalid_text) -> None:
    assert valid_text in check_text(invalid_text), 'Test1 FAIL'
