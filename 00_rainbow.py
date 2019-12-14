def print_format_table():
    s1=''
    format = ';'.join([str(style), str(fg), str(bg)])
    s1 += '\x1b[%sm %s \x1b[0m' % (
