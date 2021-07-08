import main
import pytest


@pytest.mark.parametrize("input1,input2", [("hello world", "hello world"), ("HellO WoRld", "HellO WoRld"),
                                           ("my Name is @12^^.", "my Name is @12^^."), (" ", " "), ("", ""),
                                           ("hi There 12@gmail \n", "hi There 12@gmail \n")])
def test_lower(input1, input2):
    assert main.make_lower_fun1(input1) == main.make_lower_fun1(input2)
