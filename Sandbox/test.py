x="witam serdecznie w ten piekny lutowy dzien"
def high(x):
    val=0
    highestValue=0
    highestValueWord=""
    alph="abcdefghijklmnopqrstuvwxyz"
    value=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    tab=x.split(" ")
    for i in tab:
        for j in i:
            val+=value[alph.index(j)]
            if val>highestValue:
                highestValue=val
                highestValueWord=i
    return highestValueWord

print(high(x))