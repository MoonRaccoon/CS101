def make_converter(match, replacement):
    def conv(p):
        while match in p:
            p = p.replace(match, replacement)
        return p
    return conv



def apply_converter(converter, string):
    return converter(string)