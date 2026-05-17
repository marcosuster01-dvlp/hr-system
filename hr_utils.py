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


