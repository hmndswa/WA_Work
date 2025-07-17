principal = float(input("Enter the principal amount (initial investment): "))
rate = float(input("Enter the annual interest rate (in %): "))
times_compounded = int(input("Enter the number of times interest is compounded per year: "))
years = float(input("Enter the number of years: "))

rate = rate / 100

amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
compound_interest = amount - principal

print(f"\nFinal Amount after {years} years: £{amount:.2f}")
print(f"Compound Interest earned: £{compound_interest:.2f}")
