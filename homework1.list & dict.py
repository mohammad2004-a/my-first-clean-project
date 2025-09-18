from persiantools.jdatetime import JalaliDate

def main():
    student = []
    ages = []
    while True:
        first_name = input("enter your first name : ")
        if first_name=="x":
            break
        last_name = input ("enter your last name : ")
        birthday = int(input("enter your birthday : "))
        persion = {"first_name" : first_name ,
                   "last_name":last_name ,
                   "birthaday":birthday}
        student.append(persion)
        ages.append(calculate_age(birthday))
        
    for i in range(len(student)):
        bigger_name(student[i]["first_name"],student[i]["last_name"])
        print(ages[i])
        print(20*"-")
        
    print(f"average is : {calculate_average(ages)}")
  
def bigger_name(a,b):
    big_name = (a + " " + b).upper()
    print(f"-{big_name}")
    
def calculate_age(a):
    today =  JalaliDate.today()._year
    age = today - a
    return age
    
def calculate_average(list) -> float:
    age_average = sum(list)/len(list)
    return age_average

main()
    