from datetime import datetime
from predictors import average_last_days
from heuristic import ffd

def predict_vm(ecs_lines, input_lines):
    # Do your work from here#
    result = []
    if ecs_lines is None:
        print 'ecs information is none'
        return result
    if input_lines is None:
        print 'input file information is none'
        return result

    # pm capacity
    cpu_capacity, mem_capacity, _ = [int(i) for i in ecs_lines[0].strip().split(' ')]
    mem_capacity *= 1024 
    # flavors 
    num_flavor_type = int(ecs_lines[2].strip())
    flavors = {}
    for i in range(3,3+num_flavor_type):
        flavor = ecs_lines[i].strip().split(' ')
        flavorName = flavor[0]
        cpu_size = int(flavor[1])
        mem_size = int(flavor[2])
        flavors.update({flavorName:(cpu_size,mem_size)})

    # cpu days  
    cpu_first = True if ecs_lines[3+num_flavor_type+1].strip() == 'CPU' else False
    start = datetime.strptime(ecs_lines[3+num_flavor_type+3].strip(), "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(ecs_lines[3+num_flavor_type+4].strip(), "%Y-%m-%d %H:%M:%S")


    # input
    records = []
    for line in input_lines:
        values = line.strip().split('\t')  
        uuid = values[0]
        flavorName = values[1]
        createTime = datetime.strptime(values[2], "%Y-%m-%d %H:%M:%S")
        records.append((uuid,flavorName,createTime))

    #predict
    flavors_count = average_last_days(start, end, records, up_ratio=0)
    result.append(str(sum(flavors_count.values())))
    for k in flavors.keys():
        if k not in flavors_count.keys():
            result.append(k+' '+'0')
        else:
            result.append(k+' '+str(flavors_count[k]))
    for k in flavors_count.keys():
        if k not in flavors.keys():
            flavors_count.pop(k)
    result.append('')
    #put
    put_result = ffd(flavors,flavors_count,cpu_capacity,mem_capacity,descrease=True,cpu_first=cpu_first)
    result.extend(put_result)
    return result
