#ขอบเขตตัวแปร
balance=1000 #global 
def displayBalance():
    print("ยอดเงินคงเหลือในบัญชี ",balance , " บาท")

def deposit(value):
    global balance
    money=value #local
    print("ฝากเงินจำนวน ",money , "บาท")
    balance+=money

def withdraw(value):
    global balance
    amount=value
    print("ถอนเงินจำนวน ",amount, "บาท")
    balance-=amount

displayBalance()
deposit(500)
withdraw(900)
displayBalance()