def check_fever(temperature):
  
  if temperature>=float(99.5):
    
    if temperature>float(106.7):
      print("Your fever is too high. GO TO A HOSPITAL!")
    
    elif float(100.4)<=temperature<=float(106.7):
      print("🥵 Oh No! You have a fever... Please stay home and rest today. Call your doctor if it gets worse.")
    
    elif float(99.5)<=temperature<float(100.4):
      print("You have a lowgrade fever... take it easy and maybe take of your jacket")
  
  else:
    print("Yay! You do not have a fever")

# Get temperature from user and convert to float

# temp = float(input("Enter your temperature in degrees farenheit: \n"))

# if check_fever(temp):
#   print("🥵 Oh No! You have a fever... Please stay home and rest today")

# else:
#   print("Yay! You do not have a fever.")

check_fever(float(input("Enter you temperature in degreed farenheit: \n")))