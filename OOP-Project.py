
#########################################################################################
     # THIS PROGRAM WILL MANAGE DATA OF A COLLEGE, WHICH HAS FOUR DEPARTMENTS
     # Computer Science, Agriculture, Engineering and Mathematics
     # Each Department has Faculty members & Students
#########################################################################################



# This College class is for Name and Selection of Departments
class College:
	def __init__(self, Name, Dept):
		self.Name = Name
		self.Dept = Dept

# This Faculty class contain's all the related work of Faculty
class Faculty(College):

	faculty_list = []
	Count = 0
	def __init__(self, Name, Dept, No_of_Courses, HODinfo, Exp, Qualification, Salary, Contact):
		Faculty.Count = Faculty.Count + 1
		super().__init__(Name, Dept)
		self.No_of_Courses = No_of_Courses
		self.HODinfo = HODinfo
		self.Exp = Exp
		self.Qualification = Qualification
		self.Salary = Salary
		self.Contact = Contact
		Faculty.faculty_list.append([self.Name,self.Dept,self.No_of_Courses,self.HODinfo,self.Exp,self.Qualification,self.Salary,self.Contact])

	def Add_Faculty(self):
		Name = input('Enter the Name of Faculty member: ')
		Dept = input('Enter Department of Faculty member: [CS, Agriculture, Engineering, Mathematics]: ')
		No_of_Courses = int(input('Enter No: of Courses assign: '))
		HODinfo = input('Is He/She is the HOD? Yes Or No: ')
		Exp = input('What is his/her Experience: ')
		Qualification = input('Enter his/her Qualification: ')
		Salary = input('Enter his/her Salary: ')
		Contact = int(input('Enter his/her contact Number: '))
		Faculty.faculty_list.append([Name, Dept, No_of_Courses, HODinfo, Exp, Qualification,Salary, Contact])
		print("The New Faculty Member is added successfully!")


	def SpecificFacultyMember(self):
		Empty = []
		F_Name = input("Enter the name of Faculty member which info you want: ")
		for i in Faculty.faculty_list:
			if i[0] == F_Name:
				for k in i:
					Empty.append(k)
		print("Here is the information of Faculty member named:", F_Name, "\n", Empty)

	def DepartmentHOD(self):
		D_HOD = []
		for i in Faculty.faculty_list:
			if i[3] == "Yes":
				for k in i:
					D_HOD.append(k)
		print("The |", D_HOD[1], "| department HOD name is: ", D_HOD[0])

	def ListofFaculty(self):
		print("Here is the list pattern of all Faculty Members:")
		print("[Name, Dept, No_of_Courses, HOD of Department, Experience, Qualification, Salary, Contact]")
		print(Faculty.faculty_list)


	def CountOfAllFaculty(self):
		print("There are total", Faculty.Count, "faculty members are Enrolled")





# This Student class contains all the related work about students
class Student(College):

	Count = 0
	student_list = []
	def __init__(self,Name,Dept,RollNo,Year,Contact):
		Student.Count = Student.Count + 1
		super().__init__(Name,Dept)
		self.RollNo = RollNo
		self.Year = Year
		self.Contact = Contact
		Student.student_list.append([self.Name,self.Dept,self.RollNo,self.Year,self.Contact])

	def Add_Student(self):
		name=input('Enter Name of the Student: ')
		dep=input('Enter Department of Student: [CS, Agriculture, Engineering, Mathematics]: ')
		roll=input('Enter His/Her Roll No: ')
		year=int(input('Enter His/Her Year: '))
		cont=int(input('Enter His/Her Contact Number: '))
		Student.student_list.append([name,dep,roll,year,cont])
		print("Student admission details are Added successfully in College record!")

	def Marks_of_Students(self):
		Marks = []
		Empty3 = []
		Dept = input("Enter the name of department which Test you want to take: ")
		for i in Student.student_list:
			if i[1] == Dept:
				for j in i:
					Empty3.append(j)
		Mark = int(input("Enter the test marks: "))
		Marks.append(Mark)
		print(Dept, "department student named", Empty3[0], "marks are: ", Marks)

	def ListofStudents(self):
		print("Here is the list pattern of all Students which are enrolled in the college:")
		print("[Name, Dept, RollNo, Year]")
		print(Student.student_list)

	def SpecificStudentInfo(self):
		Empty1 = []
		S_Name = input("Enter the name of Student which info you want:")
		for i in Student.student_list:
			if i[0] == S_Name:
				for k in i:
					Empty1.append(k)
		print("Here is the information of Student named:", S_Name, "\n", Empty1)

	def CountOfAllStudents(self):
		print("There are total", Student.Count, "students are Enrolled")







F = Faculty("Imran Ali","Agriculture",2,"Yes","5 Years","MS.EE","2.5 Lac",+92305627683)
S = Student("Jai","Mathematics",42,2,+923447467538)






# This total String is for providing a user mainual to the user,
# in which user have select an option related to her/her required task

print("!!  MENU FOR THE USER  !!")
print("#########################################","\n",
"Press A to Add New Faculty","\n",
"Press B to Add New Student","\n","Press C to conduct test of any department & also assign marks of that test","\n",
"Press D to Display List of Faculty Members","\n",
"Press E to Display List of Students enrolled","\n",
"Press F to Display information of specific Faculty Member his/her Name","\n",
"Press G to Display information of specific student using his/her Name","\n",
"Press H to Find out HOD of the departments","\n",
"Press I to Display count of all Faculty Members","\n",
"Press J to Display count of all Students Enrolled in college","\n",
"Press K to get Exit from program","\n","###########################################################")




while True:

	try:
		INPUT1 = input("Enter the Alphabet, Which you want to perform the specific function: ")
		if INPUT1 == "A":
			F.Add_Faculty()
			continue
		elif INPUT1 == "B":
			S.Add_Student()
			continue
		elif INPUT1 == "C":
			S.Marks_of_Students()
			continue
		elif INPUT1 == "D":
			F.ListofFaculty()
			continue
		elif INPUT1 == "E":
			S.ListofStudents()
			continue
		elif INPUT1 == "F":
			F.SpecificFacultyMember()
			continue
		elif INPUT1 == "G":
			S.SpecificStudentInfo()
			continue
		elif INPUT1 == "H":
			F.DepartmentHOD()
			continue
		elif INPUT1 == "I":
			F.CountOfAllFaculty()
			continue
		elif INPUT1 == "J":
			S.CountOfAllStudents()
			continue
		elif INPUT1 == "K":
			print("Exited from the program Successfully!")
			break



	except:
		continue