#create a dict,add datas like, roll no, name, marks,along with gender, now i want to print all the names
# and marks whose gender is male, how would you do that?
D={"roll no": [1,2,3,4,5], "Name": ["shirshak","Anurag","Gauri","Bikesh","Gita"],"Marks":[8,9,7,9,10,],"Gender":["M","M","M","M","F"]}
for i in range(len(D["roll no"])):
    if D['Gender'][i]=="M":
        print(D['Name'][i] + "=" + str(D['Marks'][i]))




