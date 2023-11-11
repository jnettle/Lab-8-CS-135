#Josh Nettle
#November 4, 2023
#CS 135
#Book(s) Price Calculator
print("Welcome to the Old College Bookstore!")
while True:
  def payment(p,q):
    payment = (p*q)+(p*0.095*q)+3*q
    return payment
  p = float(input("What is the book price? "))
  q = int(input("How many books are being bought? "))
  total_payment = payment(p,q)
  print(f"The payment amount is {total_payment:.2f}")
  repeat_request = input("Would you like to buy more books? (y/n)")
  if repeat_request == "n":
    break
print("Thank you for shopping with us!")

  
  
  
  