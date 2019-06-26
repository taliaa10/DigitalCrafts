total = input("What is your total? $")
tip_pct = input("What percentage would you like to tip? ")

def tip_calc(total, tip_pct):
  total_amt = float(total) * float(tip_pct)/100.0
  return total_amt

total_amt = tip_calc(total, tip_pct)

print(f'The amount you should tip is ${total_amt:,.2f}')