#TODO: Create a letter using starting_letter.txt
import re
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt', mode = "r") as lists:
    name_list_accurate = lists.readlines()
name_list = [re.sub(r'[\n\t\r]', '', item) for item in name_list_accurate]

for i in name_list:
    with open('Input/Letters/starting_letter.txt', mode="r") as letter:
        txt = letter.read()
    with open(f'Output/ReadyToSend/{i}.txt', mode="w") as individual:
        final_letter = txt.replace("[name]",i)
        individual.write(final_letter)