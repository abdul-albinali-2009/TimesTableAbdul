#gets number from user
userNumber = int(input("Enter a whole number: "))
#initializes counter
counter = 10
while counter <= 20:
  #prints number times counter
  print(userNumber, "x", counter, "=", userNumber * counter)
  counter = counter + 1
  #increments counter