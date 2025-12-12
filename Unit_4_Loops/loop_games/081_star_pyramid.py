height = int(input("Enter pyramid height: "))

if height < 1:
    print("Invalid height.")
else:
    for i in range(1, height + 1):
        print("*" * i)
