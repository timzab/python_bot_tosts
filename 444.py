mas=[]
s=""
# f = open("neighbour2.txt","r",encoding="utf-8")
# for line in f:
#     #line=line.strip()
#     s=s+line
#     print(s)
with open("health2.txt","r",encoding="utf-8") as f:
    for line in f:
        line = line.split('*')
        print(line)
# lines = [line.rstrip('\n') for line in open('neighbour2.txt',"r",encoding="utf-8")]
# print(lines)
    #mas.append(line.strip('*'))
    #print(line.strip('*'))
    #print(mas[0])
    #print(line)

f.close()