import requests, json, time

HEADERS = {'Authorization': 'PVEAPIToken=usr_api@pam!DG3DYUOK3982NG3298DY=79362dea-317e-42f6-8664-398457517d5c'}
URL_NODES = "https://proxmox.camara.gov.br/api2/json/nodes"
URL_RESOURCES = "https://proxmox.camara.gov.br/api2/json/cluster/resources"


class Cluster:
    def __init__(self):
        pass  

    def retorna_vm(self,vm):
        resultado = requests.get(url=URL_RESOURCES, headers=HEADERS)
        resultado = resultado.json()
        resultado = resultado['data']
        for host in resultado:
            if ((host['type'] == 'qemu') and (host['name'] == vm.get_nome())):
                vm.set_id(host['vmid'])
                node = Node()
                node.set_nome(host['node'])
                vm.set_node(node)
                vm.get_node().set_nome(host['node'])
                vm.set_memoria(host['maxmem'])
                vm.set_cpu(host['maxcpu'])
        return vm

    def lista_hosts(self):
        resultado = requests.get(url=URL_NODES, headers=HEADERS)
        resultado = resultado.json()
        dicNodes = resultado['data']
        array_nodes = []
        print(dicNodes)
        for item in dicNodes:
            node = Node()
            node.set_nome(item["node"])
            node.set_memoria(item["maxmem"])
            array_nodes.append(node)
        return array_nodes


class ItemProxmox:

    def __init__(self):
        pass

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_memoria(self):
        return self.__memoria

    def set_memoria(self, memoria):
        self.__memoria = memoria

    def get_memoria_gb(self):
        return self.get_memoria()/1024/1024/1024


class Node(ItemProxmox):

    def lista_vms(self):
        resultado = requests.get(url=URL_NODES+'/'+self.get_nome()+'/qemu', headers=HEADERS)
        resultado = resultado.json()
        dicVMs = resultado['data']
        print(self.get_nome())
        array_vms = []
        for item in dicVMs:
            vm = VM()
            vm.set_nome(item['name'])
            vm.set_memoria(item['maxmem'])
            array_vms.append(vm)
        return array_vms


class VM(ItemProxmox):

  def get_node(self):
        return self.__node
  
  def set_node(self, node):
      self.__node = node
  

  def get_cpu(self):
        return self.__cpu

  def set_cpu(self, cpu):
        self.__cpu = cpu




c = Cluster()
lista_nodes = c.lista_hosts()

for obj_node  in lista_nodes:
    print(f'Host {obj_node.get_nome()} -- { obj_node.get_memoria()}  -- Memoria em giga: { obj_node.get_memoria_gb()}')
    lista_vms = obj_node.lista_vms()
    for obj_vm in lista_vms:
        print(f'    VM:          { obj_vm.get_nome()} -- { obj_vm.get_memoria()}  -- Memoria em giga: { obj_vm.get_memoria_gb()}')
    print('###################################################')


n = Node()
n.set_nome('iridio02')
print(n.get_nome())
lista_vms = n.lista_vms()
for obj_vm in lista_vms:
  print(f'    VM:          { obj_vm.get_nome()} -- { obj_vm.get_memoria()}  -- Memoria em giga: { obj_vm.get_memoria_gb()}')


c = Cluster()
vm = VM()
vm.set_nome('teste-chavex')
vm = c.retorna_vm(vm)
print(vm.get_id())
print(vm.get_node().get_nome())
print(vm.get_cpu())
print(vm.get_memoria())
print(vm.get_nome())




