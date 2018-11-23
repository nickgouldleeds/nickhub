# Student class
class Student(object):
    def __init__(self,surname,firstname,id_number):
        self._surname = surname
        self._firstname = firstname
        self._id_number = id_number
        self._DOB = None
        self._modules = []
    def add_to_module (self,module_id):
        self._modules.append(module_id)
    
    
