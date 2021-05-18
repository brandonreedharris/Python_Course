file_builder = open("logger.txt", "w+")

#file_builder.write("Hey, I'm in a file!")

for i in range(100):
    file_builder.write(f"I'm on line {i+1}/n") # overrides all of the content in the file

file_builder.close()