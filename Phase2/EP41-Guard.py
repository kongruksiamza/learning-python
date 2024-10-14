# Guard Filter
# 100 = สอบได้คะแนนเต็ม , 50-99 = ผ่านเกณฑ์การสอบวัดผล
score=int(input("ป้อนคะแนนสอบของคุณ (50-100):"))
print("คะแนนของคุณ คือ ",score)

match score:
    case 100:
        print("สอบได้คะแนนเต็ม")
    case score if score>=50 and score<100:
        print("ผ่านเกณฑ์การสอบวัดผล")
    case _:
        print("คะแนนไม่อยู่ในเกณฑ์ที่กำหนด")