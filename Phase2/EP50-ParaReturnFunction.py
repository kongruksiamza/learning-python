#para + return function
def checkNumber(number):
    if number%2==0:
        return "เลขคู่"
    else:
        return "เลขคี่"

def summation(*data):
    total=0
    for item in data:
        total+=item
    return total
    
# result = checkNumber(13)
# print("ผลลัพธ์ = ",result)
print(summation(10,20))
print(summation(10,20,30,40,50))