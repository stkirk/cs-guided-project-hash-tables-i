# given a list that contains 2-item lists of [student_id, test_score]
# return the average of each student't top 5 scores
# return order should be in ascending order of student_id numbers

def avgScore(scores):
    # instantiate a dictionary to hold student_id and scores(lst) {score_count:1, cumulative_score: num, scores: []}
    students = {}

    # order scores by score[1] in descending order
    scores.sort(reverse=True, key=lambda value : value[1])
    # print("sorted scores-->", scores)
    # loop through score in scores
    for score in scores:
        # instantiate variables for student_id and test_score
        student_id = score[0]
        test_score = score[1]
        # if student_id in dictionary
        if student_id in students:
            # if student's top 5 scores are already stored, continue to next loop
            if students[student_id]["score_count"] == 5:
                continue
            # else increment student_id[score_count]
            students[student_id]["score_count"] += 1
            # add score to student_id[cumulative_score]
            students[student_id]["cumulative_score"] += test_score
        else:
            # create a new key (student_id) and make its value a dictionary {score_count:1, cumulative_score: score}
            students[student_id] = {"score_count": 1, "cumulative_score": test_score}

    # instantiate a list to hold lists of student_id, avg_score to append to
    average_scores = []
    # loop through the dictionary
    for student_id, score_dict in students.items():
        # append [student_id, student_id[cumulative_score] / student_id[score_count]]
        average_scores.append([student_id, int(score_dict["cumulative_score"] / score_dict["score_count"])])

    # sort array first index of each value
    average_scores.sort(key=lambda value : value[1])
    
    print(students)
    return average_scores

print(avgScore([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
# output --> [[1,87],[2,88]]
print(avgScore([[1,91],[1,91],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
print(avgScore([[1,91],[2,93]]))