#โปรแกรมตัดเกรด
#input
score = int(input("ป้อนคะแนนสอบของคุณ:"))
print("คะแนนของคุณ คือ ",score)
grade=None

#process
if score>=80 and score<=100: #80-100
    grade="A"
elif score>=70 and score<=79: #70-79
    grade="B"
elif score>=0 and score<=69: #0-69
    grade="F"
else:
    grade="N (Invalid)"

#output
print("เกรดของคุณ คือ ",grade)