'''
Created on May 25, 2015

@author: eoin
'''



class Base(object):
    
    def __init__(self):
        self.attrs = {}
        
    def __str__(self):
        return '%s'%self.attrs
    
    def test(self):
        return 'foo'
    
    def setAttr(self, key, value):
        self.attrs[key] = value
    
    
class Derived(Base):
    
    def __init__(self, base):
        self.baseattrs = base.attrs
        self.attrs = {}
    
    def setAttr(self, key, value):
        self.attrs[key] = value
        
    def getAttr(self, key):
        if key in self.attrs:
            return self.attrs[key]
        elif key in self.baseattrs:
            return self.baseattrs[key]
        return None
    
    def __str__(self):
        dictie = dict(self.baseattrs.items() + self.attrs.items())
        return '%s'%dictie


if __name__ == '__main__':
    
    root = Base()
    root.setAttr('a', 1)
    root.setAttr('b', 2)
    
    blah = Derived(root)
    blah.setAttr('c',3)
    blah.setAttr('a',666)
    print blah.test()
    print blah
    
    
