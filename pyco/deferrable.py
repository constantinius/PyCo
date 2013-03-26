
def resolve(f):
    """ Decorator for functions/methods that need a resolved state. """
    def wrap_f(self, *args, **kwargs):
        if not getattr(self, "deferred_resolved", False):
            self.deferred_resolved = self.resolve_deferred()
        return f(*args, **kwargs)
    wrap_f.name = f.name
    return wrap_f


class Deferrable(object):
    """ Interface for deferrable objects. `resolve_deferred` needs to be 
    implemented. """
    
    def resolve_deferred(self):
        raise NotImplemented("")
