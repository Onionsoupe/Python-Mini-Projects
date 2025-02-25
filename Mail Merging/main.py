
import re


with open('Input/Names/invited_names.txt', mode = "r") as lists:
    name_list_accurate = lists.readlines()
name_list = [re.sub(r'[\n\t\r]', '', item) for item in name_list_accurate]

for i in name_list:
    with open('Input/Letters/starting_letter.txt', mode="r") as letter:
        txt = letter.read()
    with open(f'Output/ReadyToSend/{i}.txt', mode="w") as individual:
        final_letter = txt.replace("[name]",i)
        individual.write(final_letter)
