# # # # s="hello"
# # # # l= list(s)
# # # # l.count('h')
# # # # print(s.upper())
# # # # print (s.lower())
# # # # print(s)
# # # # print(l)
# # #
# # #
# # # s='hello world'
# # # r='bikesh'
# # # for letter in s:
# # #     print (letter)
# # # for i in range (len(r)):
# # #     print(r[i])
# #
# #
# # #get an input from users am capitalize all of them,similarly iterate them and print individually.
# # s=input("Enter a word")
# # print(s.upper())
# # for i in s:
# #     print(i)
#
#
#
#
# #now lets join different words together like:
# #"today is monday"=>'todayismonday'
#now join our word in this way,
#today#is#monday,
#now slpit this word in to today is monday
A="Today is monday"
x=A.split()
y="".join(x)
print(y)
C=(A.replace('Today','Yesterday'))
print(C.replace('is','was'))
print("#".join(x))

