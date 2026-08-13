from ATM_Pin_verification import check_pin
def test_check_pin():
	assert check_pin(1234)=="Correct PIN"
def test_check_pin():
	assert check_pin(1111)=="Invalid PIN"
def test_check_pin():
	assert check_pin("1234")=="Invalid PIN"

