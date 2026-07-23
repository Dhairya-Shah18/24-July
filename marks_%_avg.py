#Program to calculate Total marks,Percentage and Average

print("Enter Marks of five subjects")

sub1=float(input("Subject 1:"))
sub2=float(input("Subject 2:"))
sub3=float(input("Subject 3:"))
sub4=float(input("Subject 4:"))
sub5=float(input("Subject 5:"))

total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100
average=total/5

print("Total marks :",total)
print("Percentage :",percentage,"%")
print("Average :",average)
