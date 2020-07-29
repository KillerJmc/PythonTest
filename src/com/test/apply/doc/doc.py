import os
import pydoc
import sys

from com.jmc.io.files import Files


def output_doc():
    os.makedirs('/sdcard/pydoc')
    os.chdir('/sdcard/pydoc')
    ms = list(sys.modules.keys())
    ms.extend(['str', 'numpy'])
    
    for m_name in ms:
        with open(m_name + '.txt', 'w') as f:
            sys.stdout = f
            pydoc.help(m_name)
            sys.stdout = sys.__stdout__
        

def get_method_list():
    os.chdir('/sdcard/pydoc')
    l = list()
    ms = list(sys.modules.keys())
    ms.extend(['str', 'com.jmc.io.files.Files', 'numpy'])
           
    for m_name in ms:
        try:
            s = Files.read(m_name + '.txt')
        except:
            if 'Files' in m_name:
                s = Files.read(m_name[:-6:] + '.txt')
            elif m_name == 'str':
                s = Files.read('str.txt')
        try:
            exec('import ' + m_name)    
        except:
            pass
        
        for m_method in list(eval('dir(' + m_name +')')):
            result = str()
            try:
                if not 'Files' in m_name and not 'str' in m_name:
                    pre = s[s.index(m_method + '(') : s.index('DATA')]
                else:
                    pre = s[s.index(m_method + '('):]
                    
                result = pre[:pre.index(')') + 1].replace(', /', '').replace('/', '~')
            except:
                pass
            else:   
                l.append(m_name + '.' + result)
     
    return l
    
def create_method_file(l):
    os.makedirs('/sdcard/pyms')
    os.chdir('/sdcard/pyms')
    
    for m in l:
        Files.out('', m)
        
      
      
os.chdir('/sdcard')
Files.delete('pydoc', 'pyms')        
 
output_doc()
l = get_method_list()
create_method_file(l)
   