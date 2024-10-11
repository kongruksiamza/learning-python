#match statement
service = input("ป้อนหมายเลขบริการ(1-3):")

match service:
    case "1":print("ถอนเงิน")
    case "2":print("ฝากเงิน")
    case "3":print("สอบถามยอดเงินคงเหลือในบัญชี")
    case "" :print("หมายเลขบริการไม่ถูกต้อง")