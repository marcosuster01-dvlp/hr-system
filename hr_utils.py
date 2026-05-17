def calculate_bonus(salary, performance_score):
    if performance_score == 5:
        salary_bonus = salary * 0.80
        bonus = salary_bonus - salary
    elif performance_score == 4:
        salary_bonus = salary * 0.85
        bonus = salary_bonus - salary
    elif performance_score == 3:
        salary_bonus = salary * 0.90
        bonus = salary_bonus - salary
    else:
        bonus = salary
    return bonus

def format_employee_id(name, department, hire_year):
    first = input(f"enter a name: {name}")
    second = input(f"enter a department: {department}")
    third = input(f"enter the hired year: {hire_year}")
    id = f"{first.upper()} - {second.upper()} - {third.upper()}"
    return id

def is_elegible_for_vacation(days_worked, contract_type):
    if contract_type == "full-time" & days_worked >= 90:
        return True
    elif contract_type == "part-time" & days_worked >= 180:
        return True
    else:
        return False

