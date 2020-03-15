#DO FROM SCRATCH EXERCISES ---------------------------------------------------------------------------------------------
#Files
#TODO (1): Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
#Created file called "name.py", then opens the file in write mode. Then requests users to input their full name (which is then formatted correctly via .title), it then writes this entered name into the document "name.py".
user_details = "name.py"
user_file = open(user_details, "w")

get_name = (input("Please enter your full name: "))
print(get_name.title(), file = user_file)

user_file.close()


#TODO (2): Write code that opens "name.txt" and reads the name (as above) then prints, "Your name is Bob" (or whatever the name is in the file).
#Opens the above created file, checks that is open as a read file then prints the entire contents and closes the file as finished using it.

user_file = open("name.py", 'r')
if user_file.mode == 'r':
    print(user_file.read())
user_file.close()

#TODO (3): Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers on separate lines in the file and save it: 17, 42, 400.
#Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.

user_details = "numbers.txt"
user_file = open(user_details, "r")
first_line = int(user_file.readline()) #locates value in first line and assigns to first_line variable = 17
second_line = int(user_file.readline()) #locates value in second line and assigns to first_line variable = 42
total_sum = first_line + second_line #adds the two lines together

print(total_sum) #prints the total of the first two lines in the text file "numbers.txt".
user_file.close()

#TODO (4): Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.

user_details = "numbers.txt"
user_file = open(user_details, "r")
total_sum = 0 #starting sum of 0 which is used to store the sum of the listed_numbers and then print out later
for line in user_file: #for every line listed in the user_file
    listed_numbers = int(line) #converts all the numbers listed in the text file to INT so that they can then be added together
    total_sum += listed_numbers #adds the exsiting value of 0 to all the numbers listed in the text file
print(total_sum) #prints the total sum of all the numbers in the text file.
user_file.close() #closes file.
