import pytest


def test_equal_or_not_equal():

    assert 3==3
    assert 1!=0



def is_even(n):
    return n % 2 == 0

## bool check
def test_boolean():
    assert is_even(4) == True
    assert is_even(3) == False


#variable-এর type ঠিক আছে কিনা check করা।
def test_type():
    name = "Pervez"
    assert type(name) == str


#Greater Than / Less Than Check
def test_comparison():
    value = 10

    assert value > 5
    assert value < 20

# List Check
def test_list():
    data = [1, 2, 3, 4]

    assert len(data) == 4
    assert 3 in data


# object and fixture 

class Student:
    def __init__(self,first_name:str,last_name:str,mejor:str,year:int):
        self.first_name=first_name
        self.last_name=last_name
        self.mejor=mejor
        self.year=year


@pytest.fixture
def defult_emp():
    return Student('pervez','hasan','cse',2020)



def test_person_initilization_data(defult_emp):

    assert defult_emp.first_name=='pervez','this is first name '
    assert defult_emp.last_name=='hasan','this is last name'
    assert defult_emp.mejor=='cse'
    assert defult_emp.year==2020