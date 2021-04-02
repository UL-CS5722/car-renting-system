import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj
    
    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]
    #design it to consider keys as the unique id of car
    def clone(self, name, count=1, **attr):
        """Clone a registered object and update its attributes"""
        for i in range(count):
            obj = copy.deepcopy(self._objects.get(name))
            obj.__dict__.update(attr)
            self.register_object(name, obj)
        return self._objects
