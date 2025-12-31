rice_price = 45
sugar_price = 40
oil_price = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

rice_purchased = 45*3
sugar_purchased = 40*2.5
oil_purchased = 130*1.8

print("Rice purchased =",rice_purchased)
print("Sugar purchased =",sugar_purchased)
print("Oil purchased =",oil_purchased)

total = rice_purchased+sugar_purchased+oil_purchased

print("Total amount:", total)

print("Total bill amount as integer:",int(total))

print("Total bill amount as string:",str(total))

import random
print("Total bill including delivery charge",random.randrange(5,10)+total)