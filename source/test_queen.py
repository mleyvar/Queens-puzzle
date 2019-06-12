from main import  main,getEnvironmenVar,addQueen,iniBoard



def test_getEnvironmenVar():
    assert getEnvironmenVar() == True



def test_addQueen():
    getEnvironmenVar()
    iniBoard()
    assert addQueen(0) == True

