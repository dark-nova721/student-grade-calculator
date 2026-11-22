# Student Grade Calculator 

print ("Enter your marks percentage (space separated): ")

sub_marks = [float(x) for x in input().split()]
tot_marks = 0
for marks in sub_marks:
    tot_marks += marks

avg = tot_marks/len(sub_marks)

if avg >= 90:
    print ("Grade: A")
elif avg >= 75:
    print ("Grade: B")
elif avg >= 60:
    print ("Grade: C")
else:
    print ("Grade: Needs Improvement")

print ("Average Marks:", round(avg, 2), end="")