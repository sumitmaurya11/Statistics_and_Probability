#Probability_foundations

import pandas as pd

data = {
    "customer_id": [1,2,3,4,5,6,7,8,9,10],
    "bought_coffee": [1,1,0,1,0,1,1,0,1,0],
    "bought_pastry": [1,0,1,1,0,0,1,0,1,0]
}

df = pd.DataFrame(data)
print(df.head())

#marginal probabilities P(pastry) and P(coffee).

p_coffee = df["bought_coffee"].mean()
p_pastry = df["bought_pastry"].mean()


#the joint probability P(pastry ∩ coffee).
p_joint = ((df["bought_coffee"]==1) & (df["bought_pastry"]==1)).mean()

#Axiom 4 (conditional probability) to compute P(pastry | coffee) and P(coffee | pastry).

p_pastry_given_coffee = p_joint / p_coffee
p_coffee_given_pastry = p_joint / p_pastry


#Demonstrate that P(pastry | coffee) ≠ P(coffee | pastry).

#Probability that at least one of two independent customers buys a pastry
p_buys_pastry_at_least_one = 1 - (1 - p_pastry) ** 2
p_neither_buys_pastry = (1 - p_pastry) ** 2


#Print all computed probabilities
print("=="*5,"Probability analysis module", "=="*5,)
print("P(Coffee) =" , p_coffee)
print("P(Pastry) =" , p_pastry)
print(f"P(Coffee ∩ Pastry) = {p_joint:.2f}")
print("P(Pastry | Coffee) =" , round(p_pastry_given_coffee, 4))
print("P(Coffee | Pastry) =" , round(p_coffee_given_pastry, 4))
if p_pastry_given_coffee != p_coffee_given_pastry:
    print("P(Pastry | Coffee) is not equal to P(Coffee | Pastry).")
else:
    print("P(Pastry | Coffee) is equal to P(Coffee | Pastry).")

print(f"P at least 1 of 2 independent customers buys a pastry: {p_buys_pastry_at_least_one:.4f}")
print(f"P neither of 2 independent customers buys a pastry: {p_neither_buys_pastry:.4f}")
