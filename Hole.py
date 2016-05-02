class Hole:
    count = 0
    
    def __init__(self, _address, _size):
        """
        :param _address:    Integer -> Address of Hole in memory
        :param _size:       Integer -> Size of hole
        """
        global count
        count += 1
        self.pid = count

        """
        all asserts are to make sure that we pass "int" parameters to __init__
        you are free to comment them out
        """
        assert isinstance(_address, int)
        self.address = _address
        assert isinstance(_size, int)
        self.size = _size

        """
        by default, the hole isn't allocated to any process
        so instead of the process ID, we assign it to "-1" to indicate it is free.
        """
        self.allocated_to = -1

    def __del__(self):
        global count
        count -= 1

    @staticmethod
    def merge(first, second):
        """
        :param first:   Hole -> First hole
        :param second:  Hole -> Second hole
        """

        """
        Merges a hole with another hole.
        Note that the number of holes will constantly decrease
        first, we make sure that the two holes aren't assigned to any processes
        """
        if first.allocated_to == -1 and second.allocated_to ==- 1:
                # The hole will have the least starting address of the two
                merge_address = first.address if first.address < second.address else second.address
                # The hole size will be the sum of the previous two
                merge_size = first.size + second.size
                # Delete original holes to avoid accidentally using them
                del first
                del second
                # Create the new hole
                Hole(merge_address, merge_size)
