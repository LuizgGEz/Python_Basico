from cliente import Cliente
from conta import Conta

cliente1 = Cliente("Luiz", "123.456.789-10", 40)

conta_cliente1 = Conta(cliente1, 10, 1000)

print(conta_cliente1.cliente.nome, conta_cliente1.consulta_saldo())

conta_cliente1.depositar(1000.40)

print(conta_cliente1.consulta_saldo())

conta_cliente1.sacar(500)

print(conta_cliente1.consulta_saldo())