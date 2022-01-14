multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

# The value in triple-quotes """ assigned to the multiline_str is a multi-line string literal.

# The string u"\u00dcnic\u00f6de" is a Unicode literal which supports characters other than English. In this case, \u00dc represents Ü and \u00f6 represents ö.

# r"raw \n string" is a raw string literal or (It can print \n in the string form)

print(multiline_str)
print(unicode)
print(raw_str)