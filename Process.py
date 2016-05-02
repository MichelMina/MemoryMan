class Process:

    def __init__(self, _pid, _size):
        ####all asserts are to make sure that we pass "int" parameters to __init__
        ####you are free to comment them out
        assert isinstance(_pid, int)
        self.pid = _pid
        assert isinstance(_size, int)
        self.size = _size
        ####by default, the process isn't allocated to any hole
        ####so instead of the hole ID, we assign it to "-1" to indicate it is free.
        self.allocated_to = -1

    def allocate(self, _hole):
    ####allocate the process to a hole
        ####make sure that the process isn't allocated to another hole
        ####and that the hole isn't used by another process
        if (self.allocated_to == -1 and _hole.allocated_to == -1):
            _hole.allocated_to = self
            self.allocated_to = _hole

    def deallocate(self):
    ####deallocate the process
        if self.allocated_to != -1:
            ####this part is kinda twisted :D
            ####(self.allocated_to) is hole x
            ####so self.allocated_to.allocated_to is the process to which x is allocated
            ####self.allocated_to.allocated_to means that the hole is free
            self.allocated_to.allocated_to = -1
            ####self.allocated_to = -1 means that the process isn't allocated to any hole.
            self.allocated_to = -1