#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("Input/Names/invited_names.txt") as file:
    lines=file.readlines()
with open("Input/Letters/starting_letter.txt",mode='r') as file_1:
    lines_1=file_1.read()
    print(lines_1)
for name in lines:
    names=name.strip()
    new_letter=lines_1.replace("[name]", names)
    with open(f"Output/ReadyToSend/{names}.txt",mode="w") as email:
        email.write(new_letter)