initial_deposit = int(input())
number_of_years = 0
max_deposit = 700000
interest_rate = 1.071

while initial_deposit < max_deposit:
    initial_deposit *= interest_rate
    number_of_years += 1
print(number_of_years)
