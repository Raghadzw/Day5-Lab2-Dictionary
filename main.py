dic = {
1111111111:"Amal",
2222222222:"Mohammed",
3333333333:"Khadijah",
4444444444: "Abdullah",
5555555555: "Rawan",
6666666666: "Faisal",
7777777777: "Layla"
}

x =input("Enter the phone number:")

if len(x) != 10:
    print("This is invalid number")


if x.isdigit()== False:
    print("This is invalid number")


i=int(x)
while i in dic.keys():
    y = dic.get(i)
    print(y)
    break
else:
    print("Sorry, the number is not found")












