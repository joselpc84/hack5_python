"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(result):
    if(len(result) > 3):
        if(result[0] == "f"):
            result = result[:2] + "-" + result[3:5] + "-" + result[5:7] + "-"
        if(result[0] == "b"):
            result = result[:2] + "-" + result[3:5] + "-" + result[6:8]
    if(len(result) == 3):
        result = result[:2] + "-"
    return result