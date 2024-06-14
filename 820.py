import os 
import sys 
file1 = os.access("myfile.txt",os.F_OK)
print("The file exists?:",file1)
file2 = os.access("myfile.txt",os.R_OK)
print("The file can be read?:",file2)
file3 = os.access("myfile.txt",os.W_OK)
print("The file can be written?:",file3)
file4 = os.access("myfile.txt",os.X_OK)
print("The file can be executed?:",file4)

