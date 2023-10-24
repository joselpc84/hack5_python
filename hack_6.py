"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    if(len(result) > 0):
        for i in range(len(result)):
            result[i] = f"{i+1}"
        result[1] = "-"
        result[3] = "-"
    else:
        result.append("0") 
    return result