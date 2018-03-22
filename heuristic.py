'''
heuristic algorithms 
'''
from resource import PM,VM
from collections import Counter

def ffd(flavors,flavors_count,cpu_capacity,mem_capacity,descrease=True,cpu_first=True):
    '''
    First Fit Decreasing
    '''
    vms = []
    for k,v in flavors_count.items():
        for i in range(v):
            vms.append(VM(k,flavors[k][0],flavors[k][1]))

    vms = sorted(vms, key= lambda vm:(vm.cpu_size,vm.mem_size) if cpu_first else (vm.mem_size,vm.cpu_size),reverse=descrease)
    pms = []

    for vm in vms:
        for pm in pms:
            if pm.cpu_size + vm.cpu_size <= cpu_capacity and pm.mem_size + vm.mem_size <= mem_capacity:
                pm.put(vm)
                break
        else:
            pm = PM()
            pm.put(vm)
            pms.append(pm) 
    result = []
    result.append(str(len(pms)))
    for ix,pm in enumerate(pms):
        line = []
        line.append(str(ix+1)+' ')
        vm_count = Counter([vm.flavorName for vm in pm.vms])
        for k,v in vm_count.items():
            line.append(k)
            line.append(str(v))
        result.append(' '.join(line))
    return result