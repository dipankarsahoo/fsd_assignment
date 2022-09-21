# Write a Python script to create a new file ‘myfile.txt’ and store user entered text.
# Write a Python script to read the above created file ‘myfile.txt’ and display content on
# the console.

with open('myfile.txt', 'w') as f:
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    text = '\n'.join(contents)
    f.write(text)
    
with open('myfile.txt', 'r') as f:
    text = f.read()
    print(text)