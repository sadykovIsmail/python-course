def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]  # source, auxiliary, target
    moves = []

    def move_disks(num, source, target, auxiliary):
        if num == 0:
            return
        # Move n-1 disks from source to auxiliary
        move_disks(num-1, source, auxiliary, target)
        # Move the nth disk from source to target
        disk = rods[source].pop()
        rods[target].append(disk)
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")
        # Move n-1 disks from auxiliary to target
        move_disks(num-1, auxiliary, target, source)

    moves.append(f"{rods[0]} {rods[1]} {rods[2]}")  # initial state
    move_disks(n, 0, 2, 1)  # source=0, target=2, auxiliary=1
    return "\n".join(moves)
