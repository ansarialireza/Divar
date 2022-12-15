import re
def write_file(self):
    file=open('divar.txt','a',newline='',encoding='utf-8')
    file.write(self)
    file.close()

def locatin_Regex(input):
    pattern = re.compile(r".*در.*", re.IGNORECASE)
    return pattern.match(input)