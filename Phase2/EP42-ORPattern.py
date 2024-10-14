# OR Pattern
data = input("ป้อนคำนำหน้าชื่อของคุณ:")

match data:
    case "เด็กชาย" | "นาย":
        print("เป็นเพศชาย")
    case "เด็กหญิง" | "นางสาว" | "นาง":
        print("เป็นเพศหญิง")
    case _:
        print("ไม่พบข้อมูล")