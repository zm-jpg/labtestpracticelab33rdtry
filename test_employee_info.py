import employee_info as emp


def test_get_employees_by_age_range():
    result=emp.get_employees_by_age_range(30, 40)
    expected=[{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert(result==expected)

def test_calculate_average_salary():
    result=emp.calculate_average_salary()
    expected=60166.67
    assert(result==expected)

def test_get_employees_by_dept():
    result=emp.get_employees_by_dept("Engineering")
    expected=[{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert(result==expected)