#Program to Calculate Compound Interest

principal=float(input("Enter the principal:"))
rate=float(input("Enter the rate:"))
time=float(input("Enter the time:"))

amount=principal*(1+rate/100)**time
compound_interest=amount-principal

print("Compound Interest=",round(compound_interest))
print("Total Amount=",round(amount))