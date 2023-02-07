"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    for index, scores in enumerate(student_scores):
        student_scores[index] = round(scores)
    return student_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    count = 0
    for scores in student_scores:
        if scores <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    scores_above_threshold = []
    for score in student_scores:
        if score >= threshold:
            scores_above_threshold.append(score)
    return scores_above_threshold


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    lower_threshold_scores_letter_grade = []
    factor_number = (highest - 40) / 4
    for index in range(0,4):
        if index == 0:
            lower_threshold_scores_letter_grade.append(41)
        else:
            lower_threshold_scores_letter_grade.append(int(lower_threshold_scores_letter_grade[index-1] + factor_number))
    return lower_threshold_scores_letter_grade


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    ranking = []
    for index in range(0, len(student_names), 1):
        ranking.append(f'{index + 1}. {student_names[index]}: {student_scores[index]}')
    return ranking


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    student_perfect_score=[]
    for index in range(0, len(student_info), 1):
        if int(student_info[index][1]) == 100:
            student_perfect_score = student_info[index]
            break
        
    return student_perfect_score


#student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
#print(round_scores(student_scores))

#print(count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40]))

print(above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75))

#print(letter_grades(highest=100))

#student_scores = [100, 98, 92, 86, 70, 68, 67, 60]
#student_names =  ['Rui', 'Betty', 'Joci', 'Yoshi', 'Kora', 'Bern', 'Jan', 'Rose']
#print(student_ranking(student_scores, student_names))

#print(perfect_score(student_info=[['Joci', 100], ['Vlad', 100], ['Raiana', 100], ['Alessandro', 100]]))