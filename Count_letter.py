print("😀 Welcome to the Letter Counter App ")
name=input("Enter your name here :").title().strip()
print("Hello ,"+name)

message=input("Enter your message 🖊 :")
count_alfa=input("Enter your alfabet those you want to count:")

message=message.lower()
count_alfa=count_alfa.lower()

letter_count=message.count(count_alfa)

print(f"\n {name} , your message has {letter_count} : {count_alfa} letters in it")

print("\n\nThe total alpfabet in your message 😁 .")
temp=''
for i in range (len(message)):
    if message[i] not in temp:
        print(f"{message[i]} : {message.count(message[i])}")
        temp+=message[i]
      