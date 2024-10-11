#หาผลรวมของตัวเลขไม่จำกัดจำนวน
total=0
while True:
    number = int(input("ป้อนตัวเลข:"))
    if number<=0:
        break
    total+=number

print("ผลรวม  = ",total)