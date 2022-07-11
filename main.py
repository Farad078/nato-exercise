# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas as pd
# student_data_frame = pd.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data1 = pd.read_csv("nato.csv")
letter = list(data1.letter)
code = list(data1.code)
dict = {letter[i]: code[i] for i in range(len(code))}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
answer = list(input("Enter a word: ").upper())
new_dict = [dict[k] for k in answer]
print(new_dict)


