def calculate_grade(score):
    if score > 100 or score < 0:
        return "Invalid"
    elif score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"
