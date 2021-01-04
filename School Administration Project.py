import csv

def write(info_list):
    with open('Info.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() ==0:
            writer.writerow(["Name","Age","Contact","E-Mail ID"])
        writer.writerow(info_list)
condition =  True

while(condition):
    student_info = input("Enter Student Info in Format (Name, Age, Contact Number, E-Mail ID: ")
    student_info_list = student_info.split(" ")

    write(student_info_list)

    condition = input("Enter Yes if you want to add more Data else No:")
    if condition == "Yes":
        pass
    else:
        break
