from com.jmc.io.out import new_line
from com.jmc.lang.strs import Strs

if __name__ == '__main__':
    s = """
    Hello,
    There!
    """
    print(s)
    new_line()
    print(Strs.multiline(s))





