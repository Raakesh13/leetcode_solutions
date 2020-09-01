def is_part_os_series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (2*is_part_os_series(n-1)) - (2*is_part_os_series(n-2))


for i in range(20):
    print("{} -> {}".format(i, is_part_os_series(i)))
