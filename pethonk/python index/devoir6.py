perfect_numbers = []

for n in range(1, 101):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    if divisors_sum == n:
        perfect_numbers.append(n)

print(f"les nombre parfait entre 1 et 100:{perfect_numbers}")

