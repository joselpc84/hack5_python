"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    # Lista de vocales para removerlas del string result
    vocales_list = ["a","e","i","o","u"]
    for i in result:
        if (i in vocales_list):
            result = result.replace(i, "")                     
    return result