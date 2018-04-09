i = open("sorteddata_category.txt","r")
o = open("CategoryCount_TopicWise.txt","r+")

cID = ''
cName = ''
cCount = 0		 
for line in i:	
	data = line.strip().split('\t')
	category_name,category_id = data
	if cID == "" and cName == "":
		cID = category_id	
		cName = category_name
		cCount = 1
	else:    		
		if cID == category_id and cName == category_name:
			cCount += 1
		else:
			o.write(cID +"\t"+ cName + "\t"+ str(cCount) +"\n")
			print(cID +"\t"+ cName + "\t"+ str(cCount))
			cID = category_id
			cName = category_name
			cCount = 1	
    			
i.close()
o.close()
