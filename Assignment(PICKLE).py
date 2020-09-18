import pickle

Student_details = {"Ayo":"male", "josh":"male", "goddie":"male"}

filename = "Student"    #
outfile = open(filename,'wb')

pickle.dump(Student_details, outfile)       #dumping data into puckle
outfile.close()     #closing pickle

#unpickling data
open_file = open(filename,'rb')
new_dict = pickle.load(open_file)
open_file.close()

#print data
print(Student_details)
print(type(Student_details))