##finding the ratings with nested if else
rating=0.8
op="excellent" if rating>4.5 else "good" if rating>3.5 else "average" if rating>2 else "below average" if rating>1 else "poor" 
print(op)