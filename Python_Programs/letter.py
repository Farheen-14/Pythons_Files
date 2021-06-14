letter = ''' 

Dear <|Name|>,
Greeting from Farheen Ansari!!!
I am happy to tell you about your selection.
You are selected!
Have a great day ahead.

Thanks & Regards,
Farheen Ansari
Date : <|Date|>
'''

name = input("Enter Name : ")
date = input("Enter Date : ")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)

