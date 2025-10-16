# while else

i = 1

while i <= 20:
  if i % 3 == 0 and i % 5 == 0:
    print (f'FizzBuzz -> {i}')
  elif i % 3 == 0:
    print (f'Fizz -> {i}')
  elif i % 5 == 0:
    print (f'Buzz -> {i}')
  else:
    print (i)
  i += 1