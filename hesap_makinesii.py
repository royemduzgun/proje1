def  calc(x,y,ops):

    if ops not in '+,-,*,/':
        return 'choose operator:"+,-,*,/"!'
    if ops =='+':
        return (str(x)+''+ ops +''+str(y)+'='+str(x+y))
    if ops =='-':
        return (str(x)+''+ ops +''+str(y)+'='+str(x-y))
    
    if ops =='*':
        return (str(x)+''+ ops +''+str(y)+'='+str(x*y))
    
    if ops =='/':
        return (str(x)+''+ ops +''+str(y)+'='+str(x/y))

while True:
    x=int(input('enter firs number:'))
    y=int(input('enter second number:'))
    ops=input("choose between+,-,*,/")

    print(calc(x,y,ops))

                
