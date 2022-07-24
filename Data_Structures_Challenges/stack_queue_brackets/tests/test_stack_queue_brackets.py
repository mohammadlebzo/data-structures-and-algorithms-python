import pytest
from Data_Structures_Challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets

@pytest.mark.parametrize(
    "test_string,expected",
    [
        ("{}", True),
        ("{}(){}", True),
        ("()[[Extra Characters]]", True),
        ("(){}[[]]", True),
        ("{}{Code}[Fellows](())", True),
        ("[({}]", False),
        ("(](", False),
        ("{(})", False),
    ],
)
def test_all_cases(test_string, expected):
    actual = validate_brackets(test_string)
    assert actual == expected