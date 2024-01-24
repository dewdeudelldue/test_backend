class CalculateGrade:
    
    def calculate_grade(score):
        if 80 <= score <= 100:
            return 'A'
        elif 75 <= score < 80:
            return 'B+'
        elif 70 <= score < 75:
            return 'B'
        elif 65 <= score < 70:
            return 'C+'
        elif 60 <= score < 65:
            return 'C'
        elif 55 <= score < 60:
            return 'D+'
        elif 50 <= score < 55:
            return 'D'
        else:
            return 'F'

    def calculate_gpa(subject_details):
        total_score = 0
        total_credit = 0
        for detail in subject_details:
            total_score += detail['score'] * detail['credit']
            total_credit += detail['credit']
        return total_score / total_credit
