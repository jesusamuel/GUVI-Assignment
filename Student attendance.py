a=input()
def attendance(record):
  if 'P' in record:
    c=record.count('P')
  if c >=7:
    return ('not suspended', c/10)
  else:
    return ('suspended', c/10)

print(attendance(a))
