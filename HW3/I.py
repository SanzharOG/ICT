print("Number of classes held")
a = int(input())
print("Number of classes attented")
b = int(input())
at = int((b/a)*100)
print("Your attendace is " + str(at) + "%")
if(at<75):
    print("Student is not allowed to pass exam")
else: print("Student is allowed to pass exam")