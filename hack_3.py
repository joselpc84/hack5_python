"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):
    tabla_compar = [("a","@"),("e","3"),("i","¡"),("o","0"),("u","v"),("A","@"),("E","3"),("I","¡"),("O","0"),("U","v")] 
    result = result[0].upper() + result[1:-1] + result[-1].upper()
    for i in result:
        for j in tabla_compar:
            if i in j[0]:
                result = result.replace(i,j[1])
    return result