def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode="w") as file:
        file.write(file_content)
    pass

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a") as file:
        file.write(append_content)
    pass

def read_file(file_name):
    with open(f"{file_name}.txt") as file:
        return file.read()
    pass

write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

print(read_file(file_name="logfile"))