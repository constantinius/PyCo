

SEMANTICS = {
    "x": "x",
    "y": "y",
    "z": "z",
    "time": "t"
}

class Axis(object):
    sub_axes = None
    names = ()
    
    def __init__(self, min_=None, max_=None, delta=None):
        self.min = min_
        self.max = max_
        self.delta = delta


    def transform(self, start, stop, value):
        pass
    
    
class IrregularSpacedAxis(Axis):
    def __init__(self, items):
        self.items = sorted(items)
        super(IrregularSpacedAxis, self).__init__(min(items), max(items))
    
    def transform(self, start, stop, value):
        #TODO: find out index
        pass


class ImageAxis(object):
    uom = "px"

    
class CRSAxis(Axis):
    pass


class ProjectedAxis(CRSAxis):
    uom = "m"

class GeographicAxis(CRSAxis):
    uom = "deg"
    

class LonAxis(GeographicAxis):
    semantic = "x"
    names = frozenset("lon", "long", "x")


class LatAxis(GeographicAxis):
    semantic = "y"
    names = frozenset("lat", "y")


class XAxis(ProjectedAxis):
    semantic = "x"
    names = frozenset("x")


class YAxis(ProjectedAxis):
    semantic = "y"
    names = frozenset("y")


class TimeAxis(IrregularSpacedAxis):
    semantic = "t"
    uom = "h"


class Axes(object):
    def __init__(self, sub_axes):
        self._sub_axes = tuple(sub_axes)
    
    @property
    def sub_axes(self):
        return self._sub_axes


class GeoAxes(Axes):
    def __init__(self, reference_definition, bbox):
        #TODO: load spatial reference
        sr = None
        if sr.IsProjected():
            axes = (
                XAxis(bbox[0], bbox[2], sr),
                YAxis(bbox[1], bbox[3], sr)
            )
        else:
            axes = (
                LonAxis(bbox[0], bbox[2], sr),
                LatAxis(bbox[1], bbox[3], sr)
            )
        
        super(GeoAxes, self).__init__(axes)
