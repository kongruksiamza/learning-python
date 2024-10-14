#Mapping Pattern
customers=[
    {"name":"ก้อง","type":"general"},
    {"name":"โจ้","type":"member"},
    {"name":"แนน","type":"general"}
]
id=int(input("ป้อนรหัสลูกค้า:"))
print(f"สวัสดีลูกค้ารหัส {id} : {customers[id]["name"]}")

match customers[id]:
    case {"type":"member"}:
        print("คุณเป็นสมาชิกได้รับส่วนลด 50%")
    case _:
        print("ไม่ได้รับส่วนลด")