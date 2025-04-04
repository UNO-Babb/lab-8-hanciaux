#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def makeID(first, last, ssn):
  firstInitial = first[0]
  if len(last) == 3:
    last = last + "xx"
  if len(last) == 4:
    last = last + "x"
  num = str(ssn[-3:])
  id = firstInitial + last + num

  return id

yearAB = ""
def makeMajorYear(major, year):
  major = major[0:3]
  year = year.lower()
  if year == "freshman":
    yearAB = "FR"
  if year == "sophomore":
    yearAB = "SO"
  if year == "junior":
    yearAB = "JR"
  if year == "senior":
    yearAB = "SR"

  majorYear = major.upper() + "-" + yearAB
  return majorYear

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for student in inFile:

    #student = "Antwan Dougherty AntwanDougherty@yahoo.com 443-13-3556 03/28/1996 Freshman Philosophy"

    studentData = student.split()
    lastName = studentData[1]
    firstName = studentData[0]
    ssn = studentData[3]
    year = studentData[5]
    major = studentData[6]


    studentName = lastName + "," + firstName
    userID = makeID(firstName, lastName, ssn)
    majorYear = makeMajorYear(major, year)

    studentOutput = studentName + "," + userID + "," + majorYear + "\n"
    outFile.write(studentOutput)

  
  
  



  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
