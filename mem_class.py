class Hole:

    def __init__(self, _pid, _address, _size, _allocated_to = -1):
        assert isinstance(_pid, int)
        self.pid = _pid
        assert isinstance(_address, int)
        self.address = _address
        assert isinstance(_size, int)
        self.size = _size
        assert isinstance(_allocated_to, int)
        self.allocated_to = _allocated_to

    def merge(self,other):
        merge_pid = self.pid if self.pid<other.pid else other.pid
        merge_address = self.address if self.address<other.address else other.address
        merge_size = self.size + other.size
        del other
        self.pid = merge_pid
        self.address = merge_address
        self.size = merge_size


class Process:

    def __init__(self,_pid, _size, _allocated = False):
        assert isinstance(_pid, int)
        self.pid = _pid
        assert  isinstance(_size, int)
        self.size = _size
        assert isinstance(_allocated, bool)
        self.allocated = _allocated

    def allocate(self, _hole):
        if self.allocated == False:
            _hole.allocated_to = self
            self.allocated = True

    def deallocate(self, _hole):
        if self.allocated == True:
            _hole.allocated_to = -1
            self.allocated = False

    def swap(self, _hole,):
        if (_hole.allocated_to != self ) and (_hole.allocated_to != -1) :
            _hole.allocated_to.allocated = False
            _hole.allocated_to = self


memory = []