#return keyword
balance=1000 #global 
def displayBalance():
    print("ยอดเงินคงเหลือในบัญชี ",balance , " บาท")

def deposit(value):
    global balance
    money=value #local
    print("ฝากเงินจำนวน ",money , "บาท")
    if(money<=0):
        print("ไม่สามารถฝากเงินได้")
        return 
    balance+=money

def withdraw(value):
    global balance
    amount=value
    print("ถอนเงินจำนวน ",amount, "บาท")
    if amount<=0 or amount>balance:
        print("ไม่สามารถถอนเงินได้")
        return
    balance-=amount

displayBalance()
withdraw(1001)
displayBalance()