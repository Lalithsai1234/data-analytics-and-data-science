"""
        File HANDLING
file handling is a process of adding, removing, modifying or managing the file with the programming language
1) open(file name/ file location, mode)
2)read/write
3)close()
"""
"""
Modes
r--> read
w--> write
a--> append
x--> exclusive

mode read:
1)read()
2) readline()
3)readlines()
"""
print("="*12+"read"+"="*12)
f=open("d:/10k coders/python/day51_text.txt",'r')
context= f.read() #in read(4) we can give no of characters we need
print(context)
f.close()

print("="*12+"readline"+"="*12)
f=open("d:/10k coders/python/day51_text.txt",'r')
context= f.readline()
print(context)
context=f.readline(5)#In here we can give the no of characters
print(context)
f.close()

print("="*12+"readlines"+"="*12)
f=open("d:/10k coders/python/day51_text.txt",'r')
context= f.readlines() #here also we can give characters but i will full elements that was covering charters
# context= f.readlines(7) #['hello my name is lalith\n']
# context= f.readlines(25)#['hello my name is lalith\n', 'i am from jaggayyapeta\n']
print(context)
f.close()

print("="*12+"write in w"+"="*12)
f=open("d:/10k coders/python/day51_text.txt",'w')
f.write("lalith Sai")
print("data added with write in w")
f.close()

print("="*12+"writelines in w"+"="*12)
f=open("d:/10k coders/python/day51_text.txt",'w')
f.writelines(['hello my name is lalith\n', 'i am from jaggayyapeta\n', 'i have completed my btech\n', 'before that i completed diploma'])
print("data added with write lines in w")
f.close() 

print("="*12+"write and writelines in a"+"="*12)
f=open("d:/10k coders/python/day51_text.txt",'a')
f.write("\ntechnical skills\n")
f.writelines(['python\n', 'sql\n']) #instead of using lines we can also use the for loop too
print("data added with write and writelines in a")
f.close()

print("="*12+"extra methods"+"="*12)
f=open("d:/10k coders/python/day51_text.txt",'r')
print(f.mode)       #r
print(f.encoding)   #cp1252 (it was one utf format)
print(f.writable()) #Fasle
print(f.readable()) #True
print(f.closed)     #False
f.close()
print(f.closed)     #True

