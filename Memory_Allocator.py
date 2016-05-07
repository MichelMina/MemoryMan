import Hole
import Process


def deallocate(process):
    process.deallocate()


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


def best_fit(holes, process):
    allocator(holes, process, 'b')


def worst_fit(holes, process):
    allocator(holes, process, 'w')


def first_fit(holes, process):
    allocator(holes, process, 'f')


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

if __name__ == '__main__':
    holes_given = [
        (0, 6, 0), (1, 14, 900), (2, 19, 2000), (3, 11, 2500), (4, 13, 2600)
    ]

    processes_given = [(0, 12)]

    Holes_Objects = []
    Processes_Objects = []
    # Create Holes classes
    for each in holes_given:
        Holes_Objects.append(Hole.Hole(each[2], each[1]))

    # Create Processes classes
    for each in processes_given:
        Processes_Objects.append(Process.Process(each[0], each[1]))

    for each in Processes_Objects:
        allocator(Holes_Objects, each, 'b')

    show_progress(Holes_Objects)

