def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  a = []
  for i in string_one:
    if i in string_two:
      if i not in a:
        a.append(i)
  return a
print(common_letters("saxamaphone", "barangaroo"))

# RETURNS ['a', 'o', 'n']