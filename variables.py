#simple variables to get started
message = "hello"
print(message)

#naming can only contain letters, numbers, and underscores. 
#greeting_message == ok, greeting message == error because py sees it as two different variables trying to be the same value
#be concise with the naming of variables 
	#name is better than "n", "student_name" is better than "s_n"
message = "this is a string"
message_two = 'this is also a string'
greeting = "hello "

print(message.title())
print(message.upper())
print(message.lower())

print(greeting + message)

#using whitespace in variables can help, but you can also strip whitespace if you don't need it with "rstrip()" and "lstrip()"

rspace = "there is whitespace on the right "
lspace = " there's space on the left"
print(rspace.rstrip())
print(lspace.lstrip())

#\n is a very useful tool because you can make extra lines 
extra_lines = "James\nAlbert\nJulia\nSubyn"
print(extra_lines)

