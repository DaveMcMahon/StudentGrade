#!/usr/local/bin/python3

import os
import os.path

class StudentGrader(object):

	def __init__(self):
		self.student_grades = {}

	def enter_grades(self, student_name, grade):

		self.student_name = student_name
		self.grade = grade

		print("Adding " + str(self.grade) + " to " + self.student_name + "'s grade scorecard..")
		if self.student_name in self.student_grades:
			self.student_grades[self.student_name] = self.grade
			print(str(self.grade) + " added to " + self.student_name + "'s scorecard successfully!")
		else:
			self.student_grades[self.student_name] = self.grade
		 
	def remove_student(self, student_name):
		self.student_name = student_name

		if self.student_name in self.student_grades:
			del self.student_grades[self.student_name]
			print(self.student_name + " has been removed.")
		else:
			print(self.student_name + " is not in this class list")

	def calculate_avg_grades(self, student_name):
		self.student_name = student_name

		if self.student_name in self.student_grades:
			total = 0.0
			count = 0
			avg_total = 0.0

			for key,value in self.student_grades.items():
				total += self.student_grades[self.student_name]
				count += 1
			avg_total = total / count

			print("The average total grade point average for " + self.student_name + " is: " + str(avg_total))
		else:
			print(self.student_name + " is not in this class list")

	def show_class(self):
		print(self.student_grades)

def main():

	student_grade_obj = StudentGrader()

	print("[1]	Enter Grades")
	print("[2]	Remove Student")
	print("[3]  Show the class")
	print("[4]	Exit")

	user_input = input("Welcome, What would you like to do..? (1 - 3)")
	
	while user_input != "4":
		if user_input == "1":
			student_name = input("Enter the name of the student you would like to input grades for: ")
			grade = input("Enter the grade you would like to give to " + student_name)
			student_grade_obj.enter_grades(student_name, grade)
		
		elif user_input == "2":
			student_name = input("Enter the name of the student you would like to remove: ")
			student_grade_obj.remove_student(student_name)

		elif user_input == "3":
			student_grade_obj.show_class()

		else:
			print("Quitting the program...")
			break

		user_input = input("What would you like to do now? (1 - 3)")

main()