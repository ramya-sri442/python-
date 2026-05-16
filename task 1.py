n = int(input("Enter number of students: "))
first = int(input("Enter Student 1 marks: "))
greatest = first
minimum = first
total = first
for i in range(1, n + 1):
    marks = int(input(f"Enter Student {i} marks: "))
    total += marks
    if marks > greatest:
        greatest = marks
    if marks < minimum:
        minimum = marks
average = total / n
print("Greatest =", greatest)
print("Minimum =", minimum)
print("Total =", total)
print("Average =", average)
        
        
        
        
          
          
