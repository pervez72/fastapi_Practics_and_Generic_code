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
    assert 3 in dataList Check
def test_list():
    data = [1, 2, 3, 4]

    assert len(data) == 4
    assert 3 in data