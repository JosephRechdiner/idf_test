from entities.soldier import Soldier

def sorting_soldiers(soldiers: list[Soldier]):
    for i in range(len(soldiers)):
        swapped = False
        for j in range(len(soldiers) - i - 1):
            if soldiers[j].distance < soldiers[j + 1].distance:
                soldiers[j], soldiers[j + 1] = soldiers[j + 1], soldiers[j]
                swapped = True
        if not swapped:
            break
    return soldiers