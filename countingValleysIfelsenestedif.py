def countingValleys(steps, path):
    # Write your code here
    level=0
    valley=0
    for i in range(steps):
        if(path[i]=='U'):
            level+=1
            if(level==0):
                valley+=1
        
        else:
            level-=1
        print(i,level,valley)
    return valley