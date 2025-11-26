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

def preper_inserted_not_inserted(inserted, not_inserted):
    total_inserted = len(inserted)
    total_not_inserted = len(not_inserted)
    
    result = []

    for soldier in inserted:
        result.append(soldier)

    for soldier in not_inserted:
        result.append(soldier)

    return {
        "total_inserted": total_inserted,
        "total_not_inserted": total_not_inserted,
        "all_soldiers": result
    }