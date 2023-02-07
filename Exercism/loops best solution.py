"""Making the Grade"""
def round_scores(student_scores):
    """"Round all provided student scores.
 
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    return [round(s) for s in student_scores]
def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.
 
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    return len([s for s in student_scores if s <= 40])
def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.
 
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    return [s for s in student_scores if s >= threshold]
def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.
 
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:
 
             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    step = round((highest - 41) / 4)
    return list(range(41, highest, step))
def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.
 
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    return [f'{index + 1}. {name}: {student_scores[index]}' for index, name in enumerate(student_names)]
def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.
 
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for score_set in student_info:
        if score_set[1] == 100:
            return score_set
    return []
student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
print(round_scores(student_scores))

#print(count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40]))

#print(above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75))

#print(letter_grades(highest=100))

#student_scores = [100, 98, 92, 86, 70, 68, 67, 60]
#student_names =  ['Rui', 'Betty', 'Joci', 'Yoshi', 'Kora', 'Bern', 'Jan', 'Rose']
#print(student_ranking(student_scores, student_names))

#print(perfect_score(student_info=[['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100]]))