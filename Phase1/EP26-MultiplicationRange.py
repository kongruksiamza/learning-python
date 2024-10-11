#แม่สูตรคูณแบบกำหนดช่วง
start=int(input("แม่สูตรคูณเริ่มต้น : "))
end=int(input("แม่สูตรคูณสุดท้าย : "))

for number in range(start,end+1):#2-5
    print("สูตรคูณแม่",number)
    print("-------------")
    for i in range(1,13):#1-12
        print(number,"x",i," = ",number*i)
    print("-------------")   