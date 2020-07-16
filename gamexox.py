player1=str(input("Enter the player1 name :"))
player2=str(input("Enter the player2 name :"))
player=[player1,player2]
symbol=["X","O"]
toss=["head1","tail2"]
n="1"
point1=0
point2=0
repeat=[]
count=1
import random
play=random.choice(player)
tos=random.choice(toss)
sym=random.choice(symbol)
x=player.index(play)
z=symbol.index(sym)
input1=str(input("{0} Select your toss\n  1)head\n  2)tail\n  ".format(play)))
input1=input1.lower()
print("itz",tos[:-1])
if input1 in tos:
    print(play,"You win the toss")
    print(play,"your symbol is",sym)
    print(player[x-1],"your symbol is",symbol[z-1])
    game1=play
    game2=player[x-1]
    symbol1=sym
    symbol2=symbol[z-1]
else:
    print(player[x-1],"You won the toss\n")
    print(player[x-1],"your symbol is",sym,"\n")
    print(player[x],"your symbol is",symbol[z-1],"\n")
    game1=player[x-1]
    game2=play
    symbol1=sym
    symbol2=symbol[z-1]
list1=["1","2","3"]
list2=["4","5","6"]
list3=["7","8","9"]
print(list1)
print(list2)
print(list3)
while n=="1":
 for i in range(5):
    in1=int(input("{0} Enter your input position :".format(game1)))
    length=len(repeat)
    while count==1:
      count=0
      for j in range(0,length):
        if in1==repeat[i]:
           count=count+1
      if count==1:
          print("Entered position already here !!!")
          in1=int(input("{0} Enter valid position :".format(game1)))
      while (in1 > 9) or (in1 < 1):
          print("Enter valid input !!!")
          in1=int(input("{0} Enter your input position :".format(game1)))
          count=1
    repeat.append(in1)
    count=1
    if in1 < 4:
        list1.remove(list1[in1-1])
        list1.insert(in1-1,symbol1)
    elif in1 < 7:
        list2.remove(list2[(in1-1)%3])
        list2.insert((in1-1)%3,symbol1)
    else:
        list3.remove(list3[(in1-1)%3])
        list3.insert((in1-1)%3,symbol1)
    print(list1)
    print(list2)
    print(list3)
    if list1.count(symbol1)==3 or list2.count(symbol1)==3 or list3.count(symbol1)==3 or list1[0]==list2[0]==list3[0]==symbol1 or list1[1]==list2[1]==list3[1]==symbol1 or list1[2]==list2[2]==list3[2]==symbol1 or list1[0]==list2[1]==list3[2]==symbol1 or list1[2]==list2[1]==list3[0]==symbol1:
         print(game1,"you win !")
         point1=point1+1
         print("POINTS:\n",game1,":",point1,"\n",game2,":",point2)
         break
    elif len(repeat)==9:
        print("match drawn")
        print("POINTS:\n",game1,":",point1,"\n",game2,":",point2)
    if i!=4:
     in2=int(input("{0} Enter your input position :".format(game2)))
    length=len(repeat)
    if i!=4:
     while count==1:
      count=0
      for k in range(0,length):
        if in2==repeat[i]:
           count=count+1
      if count==1:
          print("Entered position already here !!!")
          in2=int(input("{0} Enter valid position :".format(game2)))
      while in2 > 9 or in2 < 1:
          print("Enter valid input")
          in2=int(input("{0} Enter your input position :".format(game2)))
          count=1
     repeat.append(in2)
     count=1
     if in2 < 4:
        list1.remove(list1[in2-1])
        list1.insert(in2-1,symbol2)
     elif in2 < 7:
        list2.remove(list2[(in2-1)%3])
        list2.insert((in2-1)%3,symbol2)
     else:
        list3.remove(list3[(in2-1)%3])
        list3.insert((in2-1)%3,symbol2)
     print(list1)
     print(list2)
     print(list3)
     if list1.count(symbol2)==3 or list2.count(symbol2)==3 or list3.count(symbol2)==3 or list1[0]==list2[0]==list3[0]==symbol2 or list1[1]==list2[1]==list3[1]==symbol2 or list1[2]==list2[2]==list3[2]==symbol2 or list1[0]==list2[1]==list3[2]==symbol2 or list1[2]==list2[1]==list3[0]==symbol2:
         print(game2,"you win !")
         point2=point2+1
         print("POINTS:\n",game1,":",point1,"\n",game2,":",point2)
         break
    
 n=str(input("press 1 to continue again : "))
 if n=="1":
     list1=["1","2","3"]
     list2=["4","5","6"]
     list3=["7","8","9"]
     repeat.clear()
 else:
     print("__________________________________________")
