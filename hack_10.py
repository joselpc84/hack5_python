"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(result):
    result[0] = {f"{1}":f"{2}"}
    result[1] = {f"{3}",f"{4}"}
    result[2] = {f"{5}":f"{6}"}
    return result