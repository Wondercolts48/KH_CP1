# KH 2nd Crew Share projects

money_earned = float(input("How much money have you earned?: "))
crew_mem =int(input("How many crew memebers are there on the boat?: "))
divvy = money_earned - (crew_mem * 500)

crew_mem_after = crew_mem - 2

shares = divvy / crew_mem_after

captain = shares * 7
first_mate = shares * 3
crew_mem = shares - 500
print(f"The captain gets {captain:.2f}")
print(f"The first mate gets {first_mate:.2f}")
print(f"the crew members still needs {crew_mem:.2f}")