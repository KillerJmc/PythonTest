from com.jmc.io.files import Files


class Tools:
    __tempPath = '/sdcard/temp.txt'
    
    @staticmethod
    def printToTemp(s):
        Files.out(s + '\n', Tools.__tempPath, mode = 'a')
    
    @staticmethod
    def readFromTemp():
        print(Files.read(Tools.__tempPath))
        
    @staticmethod
    def delTemp():
        Files.delete(Tools.__tempPath)
