#dictionary function
colors={
    "red":"แดง",
    "green":"เขียว",
    "blue":"น้ำเงิน"
}
maincolor=colors.copy()
colors.update({"yellow":"เหลือง"}) #เพิ่ม
colors.update({"red":"แดงเข้ม"}) #แก้ไข
print(colors)
print(maincolor)