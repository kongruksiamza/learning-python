#หาผลรวมของตัวเลข 5 จำนวน
total=0
for i in range(1,6):
    number = int(input("ลำดับที่ "+str(i)+" :"))
    total+=number

print("ผลรวม = ",total)