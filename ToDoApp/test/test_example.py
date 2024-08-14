import pytest

def test_equal():
    assert isinstance(1, int)
    assert ('hello' == 'world') is False
    assert type('Hellow') is str
    flag = True
    assert flag is True
    assert 7 > 1
    num_list = [1, 2, 3]
    assert 2 in num_list
    assert all(num_list)


class Student:
    def __init__(self, first_name: str, last_name:str, major: str, year: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.year = year

@pytest.fixture
def student():
    return Student('John', 'Doe', 'Computer Science', 2023)

def test_student(student):
    assert student.first_name == 'John', 'First name is not correct'
    assert student.last_name == 'Doe', 'Last name is not correct'
    assert student.major == 'Computer Science', 'Major is not correct'
    assert student.year == 2023, 'Year is not correct'