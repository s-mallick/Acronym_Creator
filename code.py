def acronym_creator():
  name=input("enter string to create acronymn:")
  mylist=name.split(" ")#this is used to split the input, when space is encountered in the string
  acro=""
  for words in mylist:
      acro=acro+words[0].upper()
  print(acro)
acronym_creator()  
