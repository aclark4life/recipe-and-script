# Question: Can a Python package contain both a zc.buildout recipe and a setuptools console script?
# Answer: Yes!

def script():
    print 'I am a console script!'

class Recipe(object):
    def __init__(self, buildout, name, options):
        pass
    def install(self):
        print 'I am a recipe!'
        return ()
    def update(self):
        pass
