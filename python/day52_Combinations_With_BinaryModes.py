try:
    f=None
    f=open('data.txt','r')
except FileNotFoundError:
    print("exception is handled")
else:
    f.read()
finally:
    # f.close() #it will gives the name error and attribute error if f is none
    if f is not None:
        f.close()


"""
Combinations
r+ --> read+write
w+ --> write+read
a+ --> append+read
"""
print("="*12+"r+"+"="*12)
f=open("d:/10k coders/python/day52_text.txt",'r+')
print("cursor",f.tell())
print(f.read())
print("cursor",f.tell())
f.write("Lalith Sai")
print("cursor",f.tell())
f.close()

print("="*12+"w+"+"="*12)
f=open("d:/10k coders/python/day52_text.txt",'w+')
print("cursor",f.tell())
f.write("Mic College")
print("cursor",f.tell())
print(f.read())
print("cursor",f.tell())
f.close()

print("="*12+"a+"+"="*12)
f=open("d:/10k coders/python/day52_text.txt",'a+')
print("cursor",f.tell())
f.write("\n Lalith Sai \n")
print("cursor",f.tell())
print(f.read())
print("cursor",f.tell())
f.close()

print("="*12+"using with Statement"+"="*12)
with open("d:/10k coders/python/day52_text.txt",'r') as f:
    print(f.read())
    print(f.closed)
print(f.closed)    


"""
Binary Modes
rb -->read in binary
wb -->write in binary
ab -->append in binary
"""
print("="*12+"Binary Read and Write"+"="*12)
with open("d:/10k coders/python/day52_Input.png",'rb') as f:
    data=f.read()
print("Input Taken in data")
with open("d:/10k coders/python/day52_output.png",'wb') as f:
    f.write(data)
print("output added from data")


#Iteration by with odd number lines
print("="*12+"Iterating f lines"+"="*12)
i=1
f=open("d:/10k coders/python/day52_text.txt",'r')
for line in f:
    if i%2==0:
        print(line)
    i+=1
f.close()

print("="*12+"nested with statements"+"="*12)
with open("d:/10k coders/python/day52_text.txt",'r') as f:
    print("cursor of f: ",f.tell())
    with open("d:/10k coders/python/day52_text.txt",'a') as nf:
        print("cursor of nf", nf.tell())
        nf.write(f.read())
        print("cursor of nf", nf.tell())
    print("cursor of f: ",f.tell())
    print(f.read())

#it was a industry level nested with statement
# with open("d:/10k coders/python/day52_text.txt",'r') as f, with open("d:/10k coders/python/day52_text.txt",'w') as nf:
#     for line in f:
#         nf.write(line)
