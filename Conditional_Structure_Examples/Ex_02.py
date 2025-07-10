age = int(input("Enter your age: "))
day = input("What day is today ? ")

# if(age >= 18):
#     price = "$12"
#     if(day == "wednesday"):
#         price = "$10"
# else:
#     price = "$8"
#     if(day == "wednesday"):
#         price = "$6"

price = 12 if age >= 18 else 8

if(day == "wednesday"):
    # price = price - 2
    price -= 2
print("Your ticket fare is $",price)