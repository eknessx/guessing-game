for c in range(1, 10):
  for d in range(10):
    for u in range(10):
      number = 100 * c + 10 * d + u
      sum_digits = c + d + u
      product_digits = c * d * u
      if product_digits % sum_digits == 0:
        print(number)