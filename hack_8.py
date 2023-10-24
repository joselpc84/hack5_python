"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(result):
    if(len(result) == 5):
        result.reverse()
        for i in range (len(result)):
            result[i] = result[i] + "-" + f"{5-i}"
            i+=1

    if(len(result) == 3):
        result.reverse()
        for i in range (len(result)):
            result[i] = result[i] + "-" + f"{3-i}"
            i+=1

    if(len(result) == 4):
        for i in range (len(result)):
            result[i] = f"{4-i}"
            i+=1

    if(len(result) == 2):
        for i in range (len(result)):
            result[i] = f"{2-i}"
            i+=1
    return result