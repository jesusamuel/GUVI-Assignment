def ankit_max(marks_dict):
  a=list(marks_dict.values())
  a.sort(reverse=True)
  if a.count(a[0]) != len(a):
    t=[m for m in a if a[0] > m]
    for i,j in marks_dict.items() :
      if j == t[0]:
        return i
  else:
    return None
marks_dict={'Xavier': 25, 'Ibrahim': 35, 'Yatin': 25,'Sami': 25, 'Takahashi': 25}
print(ankit_max(marks_dict))
