import configparser

class ConfigurationHelper:

    configFileName = '~/.accio'

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.configFileName)
        
    def getConfigParser(self):
        return self.config

    def getFiles(self):
        return self.config.options('items')

    def getFilePath(self, nickName):
        return self.config.get('items', nickName)

    def writeFile(self, nickname, filepath):
        self.write('items', nickname, filepath)

    def setEditor(self, editorCommand):
        self.write('settings', 'editorcmd', editorCommand)
    
    def getEditor(self):
        return self.config.get('settings', 'editorcmd')

    def removeFile(self, nickname):
        print("removing " + nickname)
        self.config.remove_option('items', nickname)
        self.__saveconfig()

    def write(self, section, field, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        
        self.config[section][field] = value
        self.__saveconfig()
    
    def __saveconfig(self):
        with open(self.configFileName, 'w') as configfile:    # save
            self.config.write(configfile)