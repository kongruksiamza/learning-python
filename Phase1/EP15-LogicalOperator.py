#ตัวดำเนินการทางตรรกศาสตร์
username=input("ป้อนชื่อผู้ใช้:")
password=input("ป้อนรหัสผ่าน:")

# and or
if username=="admin" or password=="1234":
    print("เข้าสู่ระบบสำเร็จ")
else:
    print("ข้อมูลไม่ถูกต้อง")

#not 
# if not username=="admin":
#     print("เข้าสู่ระบบสำเร็จ")
# else:
#     print("ข้อมูลไม่ถูกต้อง")