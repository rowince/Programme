# hen goat problem

head = 7
legs = 16


def find_goat_hen(head, leg):
    for hen in range(head+1):
        goat = head - hen
        legs = 4 * goat + 2 * hen
        if legs == leg:
            return goat, hen
    return None, None


print(find_goat_hen(head, legs))
