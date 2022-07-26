import pytest as pytest

import main

@pytest.mark.parametrize(
    "String,expected",
    [("Estela150697+",True),("wjsd3",False),("njbjdsbcBJDB",False)]
    )

def test_password(String,expected):
    assert main.password(String) == expected



@pytest.mark.parametrize(
    "String,expected",
    [("estela",True),("wjsd3",False),("34343",False),("ana",False)]
    )
def test_nickname(String,expected):
    assert main.nickname(String) == expected


@pytest.mark.parametrize(
    "String,expected,expected2",
    [("y",True,True),("n",True,False),("g",False,False)]
    )
def test_isadmin(String,expected,expected2):
    assert main.nickname(String) == expected,expected2


