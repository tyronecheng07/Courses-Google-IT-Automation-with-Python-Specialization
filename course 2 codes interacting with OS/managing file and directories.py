#1 example 
import os

def new_directory(directory, filename):
  
  # Before creating a new directory, check to see if it already exists
  if not os.path.exists(directory):
  # Create the new file inside of the new directory
    os.mkdir(directory)
  os.chdir(directory)
  
  os.mknod(filename)
  cwd = os.getcwd()  # Get the current working directory (cwd)
  files = os.listdir(cwd)
  return files
  # Return the list of files in the new directory

print(new_directory("PythonPrograms", "script.py"))

#2 example
import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  
  with open(filename, "w") as py_file:
    py_file.write(comments)
  
  with open(filename, "r") as py_file:
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))

#3 example for csv DictReader
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as new_dict:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(new_dict)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

# example 4 csv reader
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as new_file:
    # Read the rows of the file
    rows = csv.reader(new_file)
    lst = []
    # Process each row
    for row in rows:
      lst.append(row)
    
    for row in lst[1:]:
        name, color, type = row
      # Format the return string for data rows only

        return_string += "a {} {} is {}\n".format(color,name,type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

#Call the function
print(contents_of_file("flowers.csv"))
#Call the function
print(contents_of_file("flowers.csv"))

#code list
os.path.getsize(filename) #get size
os.path.getmtime #show timestamp

#dir
os.chdir(dir) #change to a new dir path
os.mkdir(dir) #make a new dir
os.path.exists(directory) #check if exists

#to show list
path = os.getcwd()
os.listdir(path)

#create a new file
os.mknod(filename)
or with open(filename, mode): pass
