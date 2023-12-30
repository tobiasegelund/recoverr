import pytest
from recoverr import Result, Ok, Err


@pytest.mark.parametrize("v1, v2, expected", [(2, 2, True), (2, 3, False)])
def test_Result_eq(v1, v2, expected):
    ok1 = Ok(v1)
    ok2 = Ok(v2)

    assert (ok1 == ok2) == expected


@pytest.mark.parametrize("v1, v2, expected", [(2, 2, False), (2, 3, True)])
def test_Result_nq(v1, v2, expected):
    ok1 = Ok(v1)
    ok2 = Ok(v2)

    assert (ok1 != ok2) == expected
