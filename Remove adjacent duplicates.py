def deduplicate(arg):
  N_arg=arg[0]
  for i in range(1,len(arg)):
    if arg[i] != arg[i-1]:
      N_arg=N_arg+arg[i]
  return N_arg
a='ssuurruuuuuuuuuuuuuuuuuuuuuuuur'
print(deduplicate(a))
