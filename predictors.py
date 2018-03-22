from collections import Counter

def average_last_days(start, end, records, up_ratio=0.1):
    day_delta = end - start
    day_first = start - day_delta
    flavors = []
    for record in records[::-1]:
        if record[2] >= day_first:
            flavors.append(record[1])
        else:
            break
    flavors_count = Counter(flavors)
    for k,v in flavors_count.items():
        flavors_count.update({k:int(v*(1+up_ratio))})
    return flavors_count
