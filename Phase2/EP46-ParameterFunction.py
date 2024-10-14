def sayHello(time,username,age):#parameter
    print("สวัสดี ",time,username)
    print("ปีนี้คุณมีอายุ ",age," ปี")

def saveEmployee(name,department,salary):
    print(f"ชื่อ {name} , แผนก {department}")
    print(f"เงินเดือน {salary} บาท")
    print("----------------")

def showTable(num):
    print(f"---แม่ {num}------")
    for i in range(1,13):
        print(f"{num} x {i} = {num*i}")

#เรียกใช้งาน
# myTime="ตอนเช้า"
# sayHello(myTime,"ก้อง",30)#arguments
# sayHello(myTime,"โจโจ้",40)
# showTable(3)
# showTable(5)
# showTable(12)
saveEmployee("ก้อง","ไอที",30000)
saveEmployee("นัท","กราฟิก",35000)
saveEmployee("โจ้","การตลาด",50000)