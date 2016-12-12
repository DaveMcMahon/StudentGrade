#!/usr/local/bin/python3

import os
import os.path

class StudentGrader(object):

	student_grades = {}

	def enter_grades(self, student_name, grade):
		self.student_name = student_name
		self.grade = grade

		print("Adding " + str(self.grade) + " to " + self.student_name + "'s grade scorecard..")
		if self.student_name in student_grades:
			student_grades[str(self.student_name)] = int(self.grade)
			print(str(self.grade) + " added to " + self.student_name + "'s scorecard successfully!")
		else:
			student_grades.update({ str(self.student_name) : int(self.student_grades) })
		
	def remove_student(self, student_name):
		self.student_name = student_name

		if self.student_name in student_grades:
			del student_grades[self.student_name]
		else:
			print(self.student_name + " is not in this class list")

	def calculate_avg_grades(self, student_name):
		if self.student_name in student_grades:
			self.student_name = student_name
			total = 0.0
			count = 0
			avg_total = 0.0

			for key,value in student_grades.items():
				total += student_grades[self.student_name]
				count += 1
			avg_total = total / count

			print("The average total grade point average for " + self.student_name + " is: " + str(avg_total))
		else:
			print(self.student_name + " is not in this class list")

def main():

	student_grade_obj = StudentGrader()

	print("[1]	Enter Grades")
	print("[2]	Remove Student")
	print("[3]	Exit")
	user_input = input("Welcome to the grade class system. What would you like to do? (1 - 3)")

	if user_input == "1":
		student_name = input("Enter the name of the student you would like to input grades for: ")
		grade = input("Enter the grade you would like to give to " + student_name)
		student_grade_obj.enter_grades(student_name, grade)
	elif user_input == "2":
		student_name = input("Enter the name of the student you would like to remove: ")
		student_grade_obj.remove_student(student_name)
	else:
		print("Quitting the program...")
		return

main()