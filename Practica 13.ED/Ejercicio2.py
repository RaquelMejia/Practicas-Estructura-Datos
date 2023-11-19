from collections import deque

class Banco:
   def __init__(self):
       self.cola_clientes = deque()

   def llegada_cliente(self, cliente):
       self.cola_clientes.append(cliente)
       print(f"\nEl cliente {cliente} ha llegado y está en la cola.")

   def atender_cliente(self):
       if self.cola_clientes:
           cliente = self.cola_clientes.popleft()
           print(f"\nEl cliente {cliente} ha sido atendido y ha salido de la cola.")
       else:
           print("No hay clientes en la cola.")

banco = Banco()
banco.llegada_cliente("Luka Sandoval")
banco.llegada_cliente("Fernando Flores")
banco.llegada_cliente("Santiago Amaya")
banco.llegada_cliente("Zoe Ruiz")
banco.atender_cliente()

