def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score

def calc_average_score(score):
    return '{:.2f}'.format(sum([x / len(score) for x in score.values()]))

print(calc_average_score(add_score({'python' : 50},'calculus',60)))
    # loop for calculate  ผลราม 
    # find length 
    #  ฟหาค่าเแลี่ย