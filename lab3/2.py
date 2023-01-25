def add_score(subject_score, student, subject, score):
    if subject_score.get(student):
        subject_score[student].update({subject : score})
    else :
        subject_score.update({student : {subject : score}})
    return subject_score

def calc_average_score(subject_score):
    return {id : f'{sum(score for score in subject_score[id].values()) / len(subject_score[id]):.2f}' for id in subject_score}
print(add_score({ '65010773' : { 'python' : 50 }, '65010780' : {'python': 80, 'calculus': 90} },'65010773','calculus',60))
print(calc_average_score(add_score({ '65010773' : { 'python' : 50 }, '65010780' : {'python': 80, 'calculus': 90} },'65010773','calculus',60)))