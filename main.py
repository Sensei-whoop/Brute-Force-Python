everylist = []
max = input("enter the maximum possible password length");
count = 0;
def Everychar(string, count):
  if count == max:
    return
  else:
    for i in range(79):
    
      nstring = string + chr(i + 48)
      everylist.append(nstring)
      Everychar(nstring, count + 1)

Everychar("", 0)

print(everylist)


