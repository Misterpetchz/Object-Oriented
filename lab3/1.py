def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score

def calc_average_score(subject_score):
    return '{:.2f}'.format(sum(subject_score.values())/len(subject_score))
print(calc_average_score(add_score({'python' : 50},'calculus',60)))