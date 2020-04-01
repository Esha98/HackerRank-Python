number = int(input())

if number in range (1,100,2) or number in range(6,21,2):
    print("Weird")
elif number in range (2,6,2) or number in range (22,101,2):
  print("Not Weird")
else:
  print("PLease, Enter the value between 1 to 100")