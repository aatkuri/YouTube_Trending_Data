i = open("CategoryCount_TopicWise.txt","r")
o = open("CategoryCount_TopicWise_sorted.txt","w")

lines = i.readlines()
lines.sort()

for  line in lines:
    o.write(line)

i.close()
o.close()    