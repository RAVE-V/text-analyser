def count_char(f,char):
    count=0
    for c in f:
        if c == char:
          count+=1
    return count

true=1
while true:
   filename=input("         Enter The Filename  :  ")
   print("\n")
   with open(filename)as  file :
          f=file.read()

          for char in "abcdefghijklmnopqrstuvwxyz/?.>,<":
                  full =count_char(f,char)
                  print("{0} - {1}".format(char,full))
          print("\n")
          


          for char in  "abcdefghijklmnopqrstuvwxyz":
              per=100*count_char(f,char)/len(f)
              print("{0} - {1} ".format(char,round(per,2)))
          print("\n")
