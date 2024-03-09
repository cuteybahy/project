def number(no):
    sum = 0
    if(no>=0):
        for i in range (no,(2*no)+1):
            sum+= (i)
        else:
            if(no<=0):
                for i in range ((2*no),no+1):
                    sum+= (i)
        print("the sum is:",sum)
def main():
    no = int(input("enter your number:"))
    number(no)
main()
    

