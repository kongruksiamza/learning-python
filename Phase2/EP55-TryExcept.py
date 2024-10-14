try:
    number1=int(input("ป้อนตัวเลขที่ 1:"))
    number2=int(input("ป้อนตัวเลขที่ 2:"))
    result = number1/number2
    print("ผลลัพธ์ = ",result)
except ValueError:
    print("ข้อมูลไม่ถูกต้อง กรุณาป้อนข้อมูลเฉพาะตัวเลขเท่านั้น!")
except ZeroDivisionError:
    print("หารด้วยศูนย์ไม่ได้! เนื่องจากไม่ถูกนิยามในทางคณิตศาสตร์")
finally:
    print("------------")
    print("End Program")
    print("------------")