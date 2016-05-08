import Hole
import Process
import Draw

Holes_Objects = []
Processes_Objects = []
Block_List = []


def allocator(holes, process, option):
    """
    :param holes:   List -> list of Hole Objects
    :param process: Process -> Process object to allocate
    :param option:  char -> Memory Management Algorithm
                            'b' ->  Best Fit
                            'w' ->  Worse Fit
                            ELSE -> First Fit
    """
    if option is 'b':
        # Best Fit
        # Sort in ascending order according to Holes size
        holes.sort(key=lambda tup: tup.size)
    elif option is 'w':
        # Worst Fit
        # Sort in descending order according to Holes size
        holes.sort(key=lambda tup: tup.size)
        holes.reverse()

    remaining_hole = -1
    for hole in holes:
        if hole.size >= process.size:
            # Allocate and create remaining hole
            hole_size = process.size

            # new hole
            new_hole_address = hole.address + process.size
            new_hole_size = hole.size - process.size
            remaining_hole = Hole.Hole(new_hole_address, new_hole_size)

            # allocate current hole -> modify size
            hole.size = hole_size
            process.allocate(hole)
            # Show Progress
            break

    # Allocation is done -> remaining hole must be appended to Holes Objects list
    if remaining_hole is not -1:
        # append remaining hole to list
        holes.append(remaining_hole)
        return
    # Indicates that this process couldn't be allocated
    print "Couldn't allocate hole"
    # Show Progress


def fix_holes():
    to_be_removed = []
    for hole in Holes_Objects:
        if hole.size <= 0:
            to_be_removed.append(hole)

    for item in to_be_removed:
        Holes_Objects.remove(item)


def merge(in1, in2):
    """
    :param in1:   Hole -> First hole
    :param in2:   Hole -> Second hole
    """

    """
    Merges a hole with another hole.
    Note that the number of holes will constantly decrease
    first, we make sure that the two holes aren't assigned to any processes
    """
    first = Holes_Objects[in1]
    second = Holes_Objects[in2]

    if first.allocated_to == -1 and second.allocated_to == -1:
        # The hole will have the least starting address of the two

        if first.address + first.size == second.address:
            merge_address = first.address if first.address < second.address else second.address
            # The hole size will be the sum of the previous two
            merge_size = first.size + second.size
            # Delete original holes to avoid accidentally using them
            Holes_Objects.remove(first)
            Holes_Objects.remove(second)
            # Create the new hole
            Holes_Objects.append(Hole.Hole(merge_address, merge_size))


# Functions that interact with GUI
def apply_inputs(holes_given, processes_given):
    """
    :param holes_given:     List of tuples -> Holes parameters
    :param processes_given: List of tuples -> Processes parameters
    """
    # Create Holes classes
    for each in holes_given:
        Holes_Objects.append(Hole.Hole(each[1], each[2]))

    # Create Processes classes
    for each in processes_given:
        Processes_Objects.append(Process.Process(each[0], each[1]))


def best_fit():
    for each in Processes_Objects:
        allocator(Holes_Objects, each, 'b')
    fix_holes()
    Draw.draw_graph(Holes_Objects, Processes_Objects, Block_List)
    show_progress(Holes_Objects)


def worst_fit():
    for each in Processes_Objects:
        allocator(Holes_Objects, each, 'w')
    fix_holes()
    Draw.draw_graph(Holes_Objects, Processes_Objects, Block_List)
    show_progress(Holes_Objects)


def first_fit():
    for each in Processes_Objects:
        allocator(Holes_Objects, each, 'f')
    fix_holes()
    Draw.draw_graph(Holes_Objects, Processes_Objects, Block_List)
    show_progress(Holes_Objects)


def deallocate(pid):
    """
    :param pid:   Integer -> PID of process to be de-allocated
    """
    global Processes_Objects

    to_be_deleted = None
    for each in Processes_Objects:
        # Found the process
        if pid is each.pid:
            # Get the hole the process is currently allocated to
            hole_pid = each.allocated_to.pid
            # Deallocate the process
            each.deallocate()
            to_be_deleted = each
            # Merge the hole
            if hole_pid + 1 <= Hole.Hole.count:
                merge(hole_pid, hole_pid + 1)

    if to_be_deleted is not None:
        Processes_Objects.remove(to_be_deleted)

    fix_holes()
    Draw.draw_graph(Holes_Objects, Processes_Objects, Block_List)
    show_progress(Holes_Objects)


def new_process(pid, size):
    """
    :param pid:   Integer -> PID of the process to be added
    :param size:  Integer -> Size of the process to be added
    """
    Processes_Objects.append(Process.Process(pid, size))


def show_progress(holes):
    # Sort Memory by address
    holes.sort(key=lambda tup: tup.address)
    for hole in holes:
        if hole.allocated_to == -1:
            print "Free Hole:"
        else:
            print "Occupied Hole:"
            print "\tOccupied Process:\tP" + str(hole.allocated_to.pid)
        print "\tAddress:\t\t\t" + str(hole.address)
        print "\tSize:\t\t\t\t" + str(hole.size)
