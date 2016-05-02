class Process:

    def __init__(self, _pid, _size, _allocated=False):
        assert isinstance(_pid, int)
        self.pid = _pid
        assert isinstance(_size, int)
        self.size = _size
        assert isinstance(_allocated, bool)
        self.allocated = _allocated

    def allocate(self, _hole):
        if self.allocated is False:
            _hole.allocated_to = self
            self.allocated = True

    def deallocate(self, _hole):
        if self.allocated is True:
            _hole.allocated_to = -1
            self.allocated = False

    def swap(self, _hole,):
        if (_hole.allocated_to != self) and (_hole.allocated_to != -1):
            _hole.allocated_to.allocated = False
            _hole.allocated_to = self
