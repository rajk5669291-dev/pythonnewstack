# Grooming Monkey Problem

total_monkeys = int(input("Enter number of monkeys: "))
bananas = int(input("Enter total bananas: "))
eat_per_monkey = int(input("Bananas eaten per monkey: "))

fed_monkeys = bananas // eat_per_monkey
hungry_monkeys = total_monkeys - fed_monkeys

if hungry_monkeys < 0:
    hungry_monkeys = 0

print("Monkeys that can eat:", fed_monkeys)
print("Monkeys left hungry:", hungry_monkeys)
