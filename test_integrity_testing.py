from calculator import add,mul,sub
def test_add_and_mul():
	res =mul(add(1,2),2)
	assert res==6
def test_sub_and_mul():
	res =mul(sub(3,2),2)
	assert res==2

