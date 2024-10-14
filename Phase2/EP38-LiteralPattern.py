#Literal Pattern
service=100
match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")
    case 3:
        print("สอบถามยอดเงินคงเหลือ")
    case None:
        print("ข้อมูลไม่ถูกต้อง")