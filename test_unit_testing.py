from calculator import add,sub,mul,div
import pytest
def test_add():
	assert add(1,2)==3
def test_sub():
	assert sub(2,1)==1
def test_mul():
	assert mul(1,2)==2
def test_divided_zero():
	with pytest.raises(ValueError):
		div(1,0)