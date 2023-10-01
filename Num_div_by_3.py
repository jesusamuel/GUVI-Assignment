def multiple_of_3(number):
  number=str(number)
  c=0
  for i in number:
    c=c+int(i)
  while c>0:
    c=c-3
  if c==0:
    return True
  else:
    return False

number=int(input())
print(multiple_of_3(number))
