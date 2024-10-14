#Wildcard Pattern
service=0
match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")
    case 3:
        print("สอบถามยอดเงินคงเหลือ")
    case _:#default case
        print("หมายเลขบริการไม่ถูกต้อง")