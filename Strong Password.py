def checkpass(password):
  c,d,e,f=0,0,0,0
  if len(password) >= 8:
    for i in password:
      if i.isdigit():
        c=1
      elif i.isupper():
        d=1
      elif i.islower():
        e=1
      else:
        f=1
  if c+d+e+f == 4:
    return True
  else:
    return False
password='J1@123'
print(checkpass(password))
