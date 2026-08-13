from addition import add
def test_add_positive():
	assert add(10,20)==30
def test_add_negative():
	assert add(-20,-30)==-50
def test_add_zero():
	assert add(0,56)==56