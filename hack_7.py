"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(result):
    if(len(result) > 1):
        for i in range(len(result)):
            if result[i] == "a" or result[i] == "c" or result[i] == "e":
                result[i] = f"{i+1}"
            else:
                result[i] = i+1
    else:
        result[0] = 0; 
    return result