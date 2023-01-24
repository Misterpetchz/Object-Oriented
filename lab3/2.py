def add_score(subject_score, student, subject, score):
    if subject_score.get(student):
        subject_score[student].update({subject : score})
    else :
        subject_score.update({student : {subject : score}})
    return subject_score

def calc_average_score(score):
    return {[x for x in score.keys()][i] : ["{:.2f}".format(elem) for elem in [sum(score[x].values()) / len(score[x]) for x in score.keys()]][i] for i in range(len(score))}
print(add_score({ '65010773' : { 'python' : 50 }, '65010780' : {'python': 80, 'calculus': 90} },'65010773','calculus',60))
print(calc_average_score(add_score({ '65010773' : { 'python' : 50 }, '65010780' : {'python': 80, 'calculus': 90} },'65010773','calculus',60)))