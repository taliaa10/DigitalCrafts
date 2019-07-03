

def prompt_user_input():
  total_amt = float(input("What is your total? $"))
  tip_pct = float(input("What percentage would you like to tip? "))
  return (total_amt, tip_pct)


def tip_calc(total_amt, tip_pct):
  tip = total_amt * tip_pct/100.0
  return tip

def display_reciept(total_amt, tip_pct, tip_amt):
  print(f'Your total was ${total_amt:,.2f}\nYou are tipping ${tip_amt:,.2f}\nYour total is ${tip_amt + total_amt:,.2f}')
  print(".......BURGER TIME........")

(total_amt, tip_pct) = prompt_user_input()

tip_amt = tip_calc(total_amt, tip_pct)

display_reciept(total_amt, tip_pct, tip_amt)


