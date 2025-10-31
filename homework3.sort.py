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
    print(f"sort is : {sort(number)}")
    
def sort(list):
    ...
    
main()