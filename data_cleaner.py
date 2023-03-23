def convert_list(f_list):
  from unidecode import unidecode

  new_list=[]

  for i in f_list:
        if len(i) == 0:
            #print(i)
            f_list.remove(i)
        i[1]=unidecode(extracting_numbers(i[1]))
        i[2]=unidecode(extracting_numbers(i[2]))
        """
        temp=[]
        for j in i:
            #print(j)#this comment can change all the database
            a=unidecode(str(j))
            if a!='[]':
              temp.append(a)#
        new_list.append(temp)
        del temp"""
  return f_list
  
def extracting_numbers(input_str):
  import re
  my_str=input_str.replace(',','')
  f=re.findall(r'\d+', my_str)
  if len(f)!=0:
    f=f[0]
  return f

