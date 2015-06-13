# # below is Okceg v0.1
#
# def is_num(jerry):
#     try:
#         int(jerry)
#     except:
#         try:
#             float(jerry)
#         except:
#             return False
#         else:
#             return True
#     else:
#         return True
#
# print('\nInteractive Okceg Shell!\npowered by python\n')
#
# while(True):
#     i = input('>')
#
#     if i.lower() == 'exit()':
#         break
#
#     elif i[:6] == 'class(' and i[-1] == ')':
#         c = i[6:-1]
#         if is_num(c):
#             print('number')
#         elif c == 'true' or c == 'false':
#             print('boolean')
#         else:
#             print('string')
#
#     elif i[:5] == 'math(' and i[-1] == ')':
#         c = i[5:-1].split(' ')
#         o = c[0]
#         l = c[1]
#         t = c[2]
#         if l == '+':
#             print(int(o) + int(t))
#         elif l == '-':
#             print(int(o) - int(t))
#         elif l == '*':
#             print(int(o) * int(t))
#         elif l == '/':
#             print(int(o) / int(t))
#
#     else:
#         print('nonsense')

#below is Okceg v.2

__author__ = "Vibius Vibidius Zosimus"
__version__ = ".2"

print('\n')

print("Okceg IS: interactive shell of Okceg, based on python\n")

print("now i am going to say 'hello_world!'.\nhello_world!\n")

print("help:\n\tinput anything and hit 'enter';\n\tinput '1' and hit 'enter' to quit;\n")

while 1:
    user_input = input(">>> ")
    
    #first-character identifier
    print("the first character of your input is:", user_input[0])
    
    #input division
    components = []
    #step 1: get all numbers
    numbers = ""
    for jerry in user_input:
        if isinstance(jerry, int):
            numbers += jerry
    #outputting all numbers
    print("the numbers are:", numbers)
    
    #quitting
    if user_input is '1':
        break

print('\n')
