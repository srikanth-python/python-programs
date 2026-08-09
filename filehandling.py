#file handling
#write()
'''a=open("sri.txt","w")
a.write("codegnan it solutions")
a.close()

a=open("sri.txt","w")
a.write("python is a my favorate")
a.close()'''

#append()
'''a=open("sri.txt","a")
a.write("\tsrikanth")
a.close()'''

'''a=open("sri.txt","w")
a.write(input("data"))
a.close()'''

#a=open("sri.txt","w")
#read()
'''a=open("sri.txt")
#print(a.read())#it will dispaly entire content
#print(a.readline())#it will dispaly first line
#print(a.readlines())#it will display with \n
print(a.read(20))'''

#writelines()->it makes every object side by side
'''names=["sri","ramcharan","prabhas","mahesh","srikanth"]
a=open("srikanth.txt","w")
a.writelines(names)
a.close()'''


'''names=["sri","ramcharan","prabhas","mahesh","srikanth"]
a=open("srikanth.txt","w")
a.writelines("/n".join(names))
a.close()'''

'''a=open("conditions.py")
print(a.read())'''

'''a=open("C:\\Users\\Srikanth Konda\\OneDrive\\Desktop\\python\\data.py")
print(a.read())'''



