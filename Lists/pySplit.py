## Program to demonstrate the split and double split function

# The message we are going to split in order to find where I am a student
message = "From sandesyd@student.life.com Fri May 17:47:36 2022"

# find the email in order to find the school from the extension
message.strip() # Strip the white spaces
msg = message.split()
print(msg)

email = msg[1]
print(email)

# split email with the @ delimeter to find school
school = email.split('@')
print(school)

schl = school[1]
print(schl)

# split schl with the . delimeter to find school name
schl_details = schl.split('.')
print(schl_details)

school_name = schl_details[1]
print('School Name is: ', school_name.capitalize())