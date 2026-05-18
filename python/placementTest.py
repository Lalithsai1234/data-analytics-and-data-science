num=2
res=[]
temp=""
def para(temp,rcount,lcount):
    if rcount==num and lcount==num :
        res.append(temp)
        return
    if lcount<num:
        para(temp+'{',rcount, lcount+1)
    if rcount<lcount:
        para(temp+'}',rcount+1, lcount)
para(temp,0,0)
print(res) 