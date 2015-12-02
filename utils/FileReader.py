from os.path import expanduser

def readfile(relativepath):
    f = open(expanduser("~")+"/Projets/adventkata/"+relativepath, 'r')
    return f.read()
