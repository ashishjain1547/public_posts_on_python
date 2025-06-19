class Person():
    def __init__(self, pid):
        self.pid = pid
        
obama = Person(100)

obama.age = 49

print(obama.age + 2)

"""
PS C:\Users\ashish.jain50\Desktop>  & 'C:\Users\ashish.jain50\Anaconda3\python.exe' 'c:\Users\ashish.jain50\.vscode\extensions\ms-python.python-2023.8.0\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '50201' '--' 'C:\Users\ashish.jain50\Desktop\obama.py' 
51
PS C:\Users\ashish.jain50\Desktop> 
"""