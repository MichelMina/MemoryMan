class Hole:

    def __init__(self, _pid, _address, _size, _allocated_to=-1):
        assert isinstance(_pid, int)
        self.pid = _pid
        assert isinstance(_address, int)
        self.address = _address
        assert isinstance(_size, int)
        self.size = _size
        assert isinstance(_allocated_to, int)
        self.allocated_to = _allocated_to

    def merge(self, other):
        merge_pid = self.pid if self.pid < other.pid else other.pid
        merge_address = self.address if self.address < other.address else other.address
        merge_size = self.size + other.size
        del other
        self.pid = merge_pid
        self.address = merge_address
        self.size = merge_size
