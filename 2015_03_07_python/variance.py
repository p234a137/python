
def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    variance = 0.
    average = grades_average(scores)
    for score in scores:
        variance += (average - score) **2
    variance = variance / float(len(scores))
    return variance

def grades_std_deviation(variance):
    return variance ** 0.5


if __name__ == '__main__':
    grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
    print grades_variance(grades)
