"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(result):
    result.pop("bar")
    result.pop("foo")
    result["Foo"] = "Fooziman"
    return result