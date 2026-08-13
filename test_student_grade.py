from student_marks import grade
def test_grade():
	assert grade(92)=="A"
def test_grade():
	assert grade(85)=="B"
def test_grade():
	assert grade(72)=="C"
def test_grade():
	assert grade(46)=="D"
def test_grade():
	assert grade(000)=="Fail"
def test_grade():
	assert grade(-6)=="Fail"
