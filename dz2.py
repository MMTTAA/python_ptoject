textt = input("ВВЕДИТЕ СООБЩЕНИЕ >> ")
words = textt.split(" ")
smail = ""
book = {
    ":)" : '😊',
    ":(" : '☹️',
    ";)" : '😉'
    }
for t in words:
    smail += book.get(str(t), t ) + " "
print(f"UWU >> {smail}")