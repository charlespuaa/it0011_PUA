# 3.4 String Manip, File Handling 
# Pua, Charles

print("\nReading Student Information:\n")
f=open("students.txt","r")
for line in f:
    print(line)
f.close()
