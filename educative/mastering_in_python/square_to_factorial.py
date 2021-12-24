def factorial(n):
   if n == 1 or n == 0:
       return 1
   else:
        return n*factorial(n-1)

def square_factorial(n):
    return [(lambda a : a*a)(x) for x in (list(map(factorial, range(n))))]

print(square_factorial(6))