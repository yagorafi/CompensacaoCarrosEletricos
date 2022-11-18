print(f'Esse Programa irá dizer quanto será sua compesação de carbonos usando um carro eletrico (Nissan Leaf)')
valores=[]
y= float(input(f'Aperte 0 para sair ou digite a quantidade de Km rodados: '))
custoGasolina=float(344907142)
custoEletrico=float(1.7*custoGasolina)
emissaoEletrico=float(65)
emissaoGasolina=float(2280)
carbonoEletrico=float((emissaoEletrico*y)+custoEletrico)
carbonoGasolina=float((emissaoGasolina*y)+custoGasolina)
if y<0:
    print(f'não existe kilometragem negativa')
    y= float(input(f'Aperte 0 para sair ou digite a quantidade de Km rodados: '))
while y>=0:
    if carbonoGasolina<carbonoEletrico:
        print(f'Você ainda não economizou')
        print(f'Falta {(carbonoEletrico-carbonoGasolina):.2f} gramas de CO2 para começar a economizar')
    if carbonoEletrico<carbonoGasolina:
        print(f'Você economizou') 
        print(f'gora tem {(carbonoGasolina-carbonoEletrico):.2f} creditos de carbono.')
    if carbonoGasolina==carbonoEletrico:
        print(f'Você começou a economizar agora')
    valores.append(y)
    y= float(input(f'Aperte 0 para sair ou digite a quantidade de Km rodados: '))
    custoGasolina=float(344907142)
    custoEletrico=float(1.7*custoGasolina)
    emissaoEletrico=float(65)
    emissaoGasolina=float(2280)
    carbonoEletrico=float((emissaoEletrico*y)+custoEletrico)
    carbonoGasolina=float((emissaoGasolina*y)+custoGasolina)
def resultado(x):
    print(f'Os kilometros {valores}')
    print('''O Nissa Leaf consegue compensar as emissões de carbono em aproximadamente 109000 km rodados, logo é uma alternativa para o desenvolvimento limpo da tecnologia''')
    print(f'O ultimo valor digitado foi {x}')

resultado(y)
