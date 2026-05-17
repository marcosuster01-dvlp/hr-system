def calculate_bonus(salary, performance_score):
    if performance_score == 5:
        bonus = salary * 0.20
    elif performance_score == 4:
        bonus = salary * 0.15
    elif performance_score == 3:
        bonus = salary * 0.10
    else:
        bonus = 0
    return bonus

def format_employee_id(name, department, hire_year):
    id = f"{department.upper()} - {hire_year} - {name.upper()}"
    return id

def is_elegible_for_vacation(days_worked, contract_type):
    if contract_type == "full-time" and days_worked >= 90:
        return True
    elif contract_type == "part-time" and days_worked >= 180:
        return True
    else:
        return False

