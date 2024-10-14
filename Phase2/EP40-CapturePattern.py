#Capture Pattern
service=-1
match service:
    case 1:
        print("ฝากเงิน")
    case 2:
        print("ถอนเงิน")
    case 3:
        print("สอบถามยอดเงินคงเหลือ")
    case service:
        print(f"ไม่มีบริการหมายเลข {service} ในระบบ กรุณาทำรายการใหม่อีกครั้ง!")