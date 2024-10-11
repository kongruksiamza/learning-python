#nested-if
username=input("ป้อนชื่อผู้ใช้:")
password=input("ป้อนรหัสผ่าน:")

if username=="member" and password=="1234": #if หลัก
    print("เข้าสู่ระบบสำเร็จ")
    service=input("ป้อนหมายเลขบริการ(1-2):")
    if service=="1": #if ย่อย
        print("ถอนเงิน")
    elif service=="2":
        print("ฝากเงิน")
    else:
        print("หมายเลขบริการไม่ถูกต้อง")
else:
    print("ไม่พบบัญชีผู้ใช้")