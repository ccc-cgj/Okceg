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

print('\n')

print("hello_world!\n")

while 1:
    if input(">>> ") == '1':
        break

print('\n')
