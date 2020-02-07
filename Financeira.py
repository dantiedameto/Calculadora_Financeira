import math, time, os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    f = True
    while (f):
        
        print(' Calculadora Financeira Versão Alfa 9.0.1\n')
        print(''' Escolha o modelo de Conta que deseja fazer
     [ 1 ] Juros Simples
     [ 2 ] Juros Compostos
     [ 3 ] Parcelamento Postecipado
     [ 4 ] Parcelamento Antecipado
     [ 0 ] Sair
    ''')
        o = int(input(' Coloque a Opção: '))
        cls()

        if o == 1:
            print(''' Escolha o modelo de conta que deseja fazer
            Juros Simples
     [ 1 ] Descobrir o valor Futuro                    	P.[1+(i.n)]
     [ 2 ] Descobrir o valor Principal                 	P/[1+(i*n)]
     [ 3 ] Descobrir o Valor Presente                  	F/[1+(i*n)]
     [ 4 ] Descobrir o Tempo                           	[(F/P)-1]/i
     [ 5 ] Descobrir a Taxa                            	[(F/P)-1]/n
     [ 6 ] Voltar
     [ 0 ] Sair''')
            op = int(input('\n Coloque a Opção: '))
            cls()

        # Juro Simples
            if op == 1:
                print('\n A formula utilizada para esta conta é  P.[1+(i.n)] \n')
                p = float(input('Coloque o valor do Capital: '))
                n = float(input('Coloque o tempo: '))
                i = float(input('Coloque a taxa: '))

                it = i / 100
                o1 = p * (1 + (it * n))

                print(' O resultado do valor fururo é:{:.2f}'.format(o1))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()

            elif op == 2:
                print('\n A formula utilizada para esta conta é  P/[1+(i*n)] \n')
                p = float(input(' Coloque o valor do Capital: '))
                n = float(input(' Coloque o tempo: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                o15 = p / (1 + (it * n))
                print(' O resultado do valor fururo é: {:.2f}'.format(o15))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 3:
                print('\n A formula utilizada para esta conta é  F/[1+(i*n)] \n')
                f = float(input(' Coloque o valor Futuro: '))
                n = float(input(' Coloque o tempo: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                o2 = f / (1 + (it * n))
                print(' O valor principal é: {:.2f}'.format(o2))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 4:
                print('\n A formula utilizada para esta conta é  [(F/P)-1]/i \n')
                f = float(input(' Coloque o valor Futuro: '))
                p = float(input(' Coloque o valor do Capital: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                o3 = (((f / p) - 1) / it)
                print(' O tempo utilizado na transação foi:{:.4f}'.format(o3))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 5:
                print('\n A formula utilizada para esta conta é  [(F/P)-1]/n \n')
                f = float(input(' Coloque o valor Futuro: '))
                p = float(input(' Coloque o valor do Capital: '))
                n = float(input(' Coloque o tempo: '))

                o4 = (((f / p) - 1) / n)
                print(' A taxa utilizada na transação foi de: {:.2f}%'.format(o4 * 100))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 6:
                menu() 
            
            elif op == 0:
                print('\n Criado por Dantie & Brendow Copyright 2019')
                time.sleep(2)
                f = False

        elif o == 2:
            print(''' Juros Compostos
     [ 1 ] Descobrir o valor Futuro                    	P.[(1+i)^n]
     [ 2 ] Descobrir o valor Futuro invertido          	P/[(1+i)^n]
     [ 3 ] Descobrir o valor Principal                 	F/[(1+i)^n]
     [ 4 ] Descobrir o Tempo                           	Log(F/P) / Log(1+i)
     [ 5 ] Descobrir a Taxa                            	[((F/P) ^ (1/n))-1].100
     [ 6 ] Voltar
     [ 0 ] Sair''')
            op = int(input('\n Coloque a Opção: '))
            cls()

        # Juros Composto
            if op == 1:
                print('\n A formula utilizada para esta conta é  P.[(1+i)^n] \n')
                p = float(input(' Coloque o valor do Capital: '))
                n = float(input(' Coloque o tempo: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                o5 = p * (1 + it) ** n
                print(' O resultado do valor fururo é: {:.2f}'.format(o5))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 2:
                print('\n A formula utilizada para esta conta é  P/[(1+i)^n] \n')
                p = float(input(' Coloque o valor do Capital: '))
                n = float(input(' Coloque o tempo: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                o60 = p / (1 + it) ** n
                print(' O resultado do valor fururo é: {:.2f}'.format(o60))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 3:
                print('\n A formula utilizada para esta conta é  F/[(1+i)^n] \n')
                f = float(input(' Coloque o valor Futuro: '))
                n = float(input(' Coloque o tempo: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                o6 = f / ((1 + it) ** n)
                print(' O valor principal é: {:.2f}'.format(o6))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 4:
                print('\n A formula utilizada para esta conta é  Log(F/P) / Log(1+i) \n')
                f = float(input(' Coloque o valor Futuro: '))
                p = float(input(' Coloque o valor do Capital: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                l1 = f / p
                lo1 = math.log(l1)
                l2 = 1 + it
                lo2 = math.log(l2)
                o7 = lo1 / lo2
                print(' O tempo utilizado na transação foi:{:.4f}'.format(o7))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 5:
                print('\n A formula utilizada para esta conta é  [((F/P) ^ (1/n))-1].100 \n')
                f = float(input(' Coloque o valor Futuro: '))
                p = float(input(' Coloque o valor do Capital: '))
                n = float(input(' Coloque o tempo: '))

                p1 = f / p
                p2 = 1 / n
                p3 = p1 ** p2
                p4 = p3 - 1
                o8 = p4 * 100
                print(' A taxa utilizada na transação foi de: {:.3f}%'.format(o8))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 6:
                menu() 

            elif op == 0:
                print('\n Criado por Dantie & Brendow Copyright 2019')
                time.sleep(2)
                f = False

        elif o == 3:
            print(''' Parcelamento
     [ 1 ] Descobrir Parcela                          	P.(i.(1+i^n))/((1+i^n)-1)
     [ 2 ] Descobrir o valor Presente                 	P.((1+i^n)-1)/(i.(1+i^n))
     [ 3 ] Descobrir valor Futuro Invertido           	P/[((1+i^n)-1)/i]
     [ 4 ] Descobrir o Valor futuro Certo             	P.[((1+i^n)-1)/i]
     [ 5 ] Descobrir o Tempo                          	Log [P/(P-(n.i))] / Log (1+i)
     [ 6 ] Voltar
     [ 0 ] Sair''')

            op = int(input('\n Coloque a Opção: '))
            cls()

        # Parcelamento
            if op == 1:
                print('\n A formula utilizada para esta conta é  P.(i.(1+i^n))/((1+i^n)-1) \n')
                p = float(input(' Coloque o valor Presente: '))
                n = float(input(' Coloque o tempo: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                lu = it + 1
                p9 = p * (it * (lu ** n)) / ((lu ** n) - 1)
                print(' O resultado do valor fururo é: {:.2f}'.format(p9))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 2:
                print('\n A formula utilizada para esta conta é  P.((1+i^n)-1)/(i.(1+i^n)) \n')
                p = float(input(' Coloque o valor da Parcela: '))
                n = float(input(' Coloque o tempo: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                lu = it + 1
                p10 = p * ((lu ** n) - 1) / (it * (lu ** n))
                print(' O valor principal é: {:.2f}'.format(p10))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 3:
                print('\n A formula utilizada para esta conta é  P/[((1+i^n)-1)/i] \n')
                p = float(input(' Coloque o valor da Parcela: '))
                n = float(input(' Coloque o valor do Tempo: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                lu = it + 1
                p11 = p / (((lu ** n) - 1) / it)

                print(' O tempo utilizado na transação foi:{:.2f}'.format(p11))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 4:
                print('\n A formula utilizada para esta conta é  P.[((1+i^n)-1)/i] \n')
                p = float(input(' Coloque o valor da Parcela: '))
                n = float(input(' Coloque o valor do Tempo: '))
                i = float(input(' Coloque a taxa: '))

                it = i / 100
                lu = it + 1
                p12 = p * (((lu ** n) - 1) / it)

                print(' O tempo utilizado na transação foi:{:.2f}'.format(p12))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 5:
                print('\n A formula utilizada para esta conta é  Log [P/(P-(n.i))] / Log (1+i) \n')
                p = float(input(' Coloque o valor da Parcela: '))
                n = float(input(' Coloque o valor Presente: '))
                i = float(input(' Coloque a Taxa: '))

                it = i / 100
                l1 = p / (p - (n * it))
                l2 = (1 + it)
                lo1 = math.log(l1)
                lo2 = math.log(l2)
                p13 = lo1 / lo2
                print(' O tempo utilizado na transação foi:{:.2f}'.format(p13))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 6:
                menu()

            elif op == 0:
                print('\n Criado por Dantie & Brendow Copyright 2019')
                time.sleep(2)
                f = False


        elif o == 4:
            print(''' Parcelamento
     [ 1 ] Parcelamento com entrada        	pmt.((((1+i)^n+1)-1)-i)/((1+i^n).1)
     [ 2 ] Descobrir o valor da parcela   	(((p.i.)1+i^n)/((((1+i)^n+1)-1)-i)
     [ 3 ] Descobrir o valor Futuro        	F = pmt.((((1+i)^n+1)-1)-i)/i
     [ 4 ] Descobrir o valor da parcela tendo o valor futuro pmt=(f.i)/((((1+i)^n+1)-1)-i)
     [ 5 ] Voltar
     [ 0 ] Sair''')
            op = int(input('\n Coloque a Opção: '))
            cls()

            if op == 1:
                print('\n A formula utilizada para esta conta é  pmt.((((1+i)^n+1)-1)-i)/((1+i^n).i) \n')
                pmt = float(input(' Coloque o valor da Parcela: '))
                n = float(input(' Coloque o Tempo: '))
                i = float(input(' Coloque a Taxa: '))

                it = i / 100
                ak = 1 + it
                al = n + 1
                p14 = pmt * (((ak ** al) - 1) - it) / ((ak ** n) * it)

                print(' O Resutado é:{:.2f}'.format(p14))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 2:
                print('\n A formula utilizada para esta conta é  (((p.i.)1+i^n)/((((1+i)^n+1)-1)-i) \n')
                p = float(input(' Coloque o valor Presente: '))
                n = float(input(' Coloque o tempo: '))
                i = float(input(' Coloque a Taxa: '))

                it = i / 100
                ak = 1 + it
                al = n + 1
                p15 = (p * i * (ak ** n)) / (((ak ** al) - 1) - it) / 100

                print(' O Resutado é:{:.9f}'.format(p15))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 3:
                print('\n A formula utilizada para esta conta é  F = pmt.((((1+i)^n+1)-1)-i)/i \n')
                pmt = float(input(' Coloque o valor da Parcela: '))
                n = float(input(' Coloque o Tempo: '))
                i = float(input(' Coloque a Taxa: '))

                it = i / 100
                ak = 1 + it
                al = n + 1
                p16 = pmt * (((ak ** al) - 1) - it) / it

                print(' O Resutado é:{:.2f}'.format(p16))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 4:
                print('\n A formula utilizada para esta conta é  pmt=(f.i)/((((1+i)^n+1)-1)-i) \n')
                f = float(input(' Coloque o valor total do Financiamento: '))
                n = float(input(' Coloque o valor Tempo: '))
                i = float(input(' Coloque a Taxa: '))

                it = i / 100
                ak = 1 + it
                al = n + 1
                p17 = (f * it) / (((ak ** al) - 1) - it)
                
                print(' O Resutado é:{:.2f}'.format(p17))
                not input('''\n Pegue o resultado antes de proseguir pois ele será apagado
        \n Aperte enter para Continuar''')
                cls()
                menu()
                
            elif op == 5:
                menu()

            elif op == 0:
                print('\n Criado por Dantie & Brendow Copyright 2019')
                time.sleep(2)
                f = False

        # SAIR
        elif o == 0:
            print('\n Criado por Dantie & Brendow Copyright 2019')
        time.sleep(2)
        f = False

print(menu())

