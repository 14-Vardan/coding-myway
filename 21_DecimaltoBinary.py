def decimaltobin(dec):
    bnum=[]
    div=int()
    d=num
    while(d>1):
      remd=d%2
      bnum.append(remd)
      div=d//2
      d=div

    bnum.append(div)
    bnum.reverse()
    binary=""
    for item in bnum:
       binary=binary + str(item)

    return print(f"The Binary Equivalent for {num} is:\n {binary}")

num=int(input("Enter a number to Find its binary equivalent:"))
decimaltobin(num)


