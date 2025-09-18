def main():
    number = []
    while True:
        a  = int(input("enter number : "))
        number.append(a)
        if len(number) > 10 :
            print("cuntniue ?")
            b = input()
            if b == "n":
                break
    print(f"maximum is : {maximum(number)}") 
      
def maximum(list):
    maximum = list[0]
    for i in list:
        if i > maximum:
            maximum = i
    return maximum
    
main()

