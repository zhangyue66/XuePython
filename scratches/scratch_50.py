names =["Yue","Lingzi","Minshan","fangfang",'Yinqi']

courses =["Chinese","Maths","English"]

scores = [[None]*len(courses) for _ in range(len(names))]
for row,name in enumerate(names):
    for column,course in enumerate(courses):
        scores[row][column]=float(input(f"please enter {name}'s {course}'s score:"))
print(scores)
print(f"{names[3]}'s {courses[1]} is {scores[3][1]}")