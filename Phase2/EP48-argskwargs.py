#args / kwargs
# ข้อมูลแบบลำดับ *args
# ข้อมูลแบบกำหนดชื่อ **kwargs

def saveEmployee(**kwargs): #dictionary
    print(f"ชื่อพนักงาน {kwargs["name"]} , แผนก {kwargs["department"]}")
    print(f"เงินเดือน {kwargs["salary"]} บาท")
    print(f"ที่อยู่ {kwargs["country"]} ")
    print("----------------")


#เรียกใช้งาน
saveEmployee(name="ก้อง",department="ไอที",salary=30000,country="ภูเก็ต")
saveEmployee(name="นัท",department="กราฟิก",salary=35000,country="อุดรธานี")
saveEmployee(name="โจ้",department="การตลาด",salary=50000,country="น่าน")