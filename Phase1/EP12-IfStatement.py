#input
score = int(input("กรุณาป้อนคะแนนสอบของคุณ:"))
print("คะแนนสอบของคุณ =",score)

#process
if score<0:
    print("คะแนนไม่ถูกต้อง")
elif score>=50:
    print("A")
else:
    print("F")