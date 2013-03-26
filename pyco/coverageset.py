from pyco.deferrable import Deferrable, resolve


class CoverageSet(object):
    def __init__(self, coverages=None):
        self.coverages = coverages if coverages is not None else []
        
    def filter(self, *args, **kwargs):
        coverages = self.coverages[:]
        for f in args:
            coverages = filter(f, coverages) 
        
        return type(self)(coverages)
    
    def __iter__(self):
        return iter(self.coverages)
    
    def add(self, coverage):
        self.coverages.append(coverage)
    

class DeferredCoverageSet(CoverageSet, Deferrable):
    
    @resolve
    def __iter__(self):
        return iter(self.coverages)
