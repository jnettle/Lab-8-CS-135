#Edit 1 to interest program
#Josh Nettle
#November 4, 2023
#CS 135
#Monthly Payment/Interest Calculator
import math
computation_count = 1
while True:
  def payment(p,r,n):
    payment = p*(R*math.pow(1+R, N))/(math.pow(1+R, N)-1)
    return payment
  p = float(input("How much is the loan? "))
  r = float(input("Annual interest rate? "))
  n = float(input("How many years? "))
  R = ((r/12)/100)
  N = n*12
  monthly_payment = payment(p,r,n)
  print(f"the monthly payment is ${monthly_payment:.2f}")
  repeat_request = input("Would you like to compute the monthly payment again? y/n")
  if repeat_request == "n":
      break
  computation_count += 1
print(f"The monthly payment value has been computed {computation_count} time(s) today.")
