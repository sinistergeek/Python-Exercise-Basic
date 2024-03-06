import pickle

student = {'rollno':205,'name':'sinister','age':19}
f = open('student.txt','ab')
pickle.dump(student,f) #write on file 
# load the file
f.close()
