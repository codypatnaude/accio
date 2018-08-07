import sys
from termcolor import colored, cprint
import configuration
import re

def listFiles(pattern):
    
    #read the file nicknames that have been added to the system
    conf = configuration.ConfigurationHelper()
    items = conf.getFiles()
    maxLength = len(max(items, key=len))

    #filter out nicknames that don't match pattern
    if(pattern):
        items = filter(lambda elem: re.match(r"^{0}.*".format(pattern), elem), items)
        print('filtered items')
        print(items)
        
    #get filenames that are associated to matching nicks. Store in a way that's easy to display
    output = map(lambda el: [str(el).ljust(maxLength + 4), conf.getFilePath(el)], items)
    
    for item in output:
        print("\t" + '\033[01;32m' + item[0] + '\033[94m' + item[1])
        #set color back to default
        sys.stdout.write('\033[m')
