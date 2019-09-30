marksheet = []
numberOfStudents = int(input())
for N in range(0,numberOfStudents):
    student = input()
    mark = float(input())
    marksheet.append([student, mark])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
