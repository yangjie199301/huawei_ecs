'''
resource class
'''
class PM(object):
    def __init__(self):
        self.vms = []
        self.cpu_size = 0
        self.mem_size = 0

    def put(self, vm):
        self.vms.append(vm)
        self.cpu_size += vm.cpu_size
        self.mem_size += vm.mem_size

    def __str__(self):
        return 'PM(cpu_size=%d cores, mem_size=%d MB, vms=%s)' % (self.cpu_size, self.mem_size, str(self.vms))

class VM(object):
    def __init__(self,flavorName,cpu_size,mem_size):
        self.flavorName = flavorName
        self.cpu_size = cpu_size
        self.mem_size = mem_size
        
    def __str__(self):
        return self.flavorName