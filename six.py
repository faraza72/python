if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    print student_marks
    if query_name in student_marks:
        a = student_marks[query_name]
    print "%.2f" % (sum(a) / len(a))