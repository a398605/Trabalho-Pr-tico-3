from datetime import datetime


class Veiculos(object):
    def __init__(self, marca="", modelo="", ano=0, valor=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.codigo = ""
        self.status = "DISPONÍVEL"


Codigos = []
Marca = []
Modelo = []
Ano = []
Valor = []
Status = []
Ialuguel = []
Faluguel = []
Cliente = []
Prazo = []
objetos = []
comando = 0
now = datetime.now()
Dia = now.day
Mes = now.month
Anos = int(now.year)

while comando != 7:
    print("######### LOCADORA [LOCALIZA] #######")
    print("\n\tDATA: |{} \ {} \ {}|\n".format(Dia, Mes, Anos))
    print("Digite [1] para |Adicionar Veículos|.")
    print("Digite [2] para |Consultar Veículos|.")
    print("Digite [3] para |Alugar/reservar Veículos|.")
    print("Digite [4] para |Devolver/Liberar Veículos|.")
    print("Digite [5] para |Excluir Veículos|.")
    print("Digite [6] para |Avançar data atual|.")
    print("Digite [7] Para ""SAIR"" ")
    comando = int(input("Digite qual operação deseja realizar: "))
    print("")
    if comando == 1:
        print("############# CADASTRO DE VEÍCULOS #############\n")
        print("-----------------------------------")
        a = input("MARCA:")
        b = input("MODELO:")
        c = input("ANO:")
        d = input("VALOR DA DIÁRIA DO VEÍCULO:")
        print("-----------------------------------\n")
        Marca.append(a)
        Modelo.append(b)
        Ano.append(c)
        Valor.append(d)
        e = len(Modelo)
        Codigos.append("00"+str(e))
        obj = Veiculos()
        obj.codigo = e
        obj.valor = float(d)
        obj.ano = int(c)
        obj.modelo = b
        obj.marca = a
        objetos.append(obj)
        Status.append(obj.status)
        Ialuguel.append(str(Dia)+str(Mes)+str(Anos))
        Faluguel.append("")
        Cliente.append("")
        Prazo.append(0)
        print("================================================\n")
    if comando == 2:
        print("")
        print("######## CONSULTAR VEÍCULOS #########\n")
        NumdeCarros = len(Codigos)
        c = 0
        print("***********************************")
        while c < NumdeCarros:
            print("|{}--{}--{}|".format(Codigos[c], Modelo[c], Status[c]))
            c = c + 1
            print("***********************************")
        print("\nDigite 1 para Consulta Mais Detalhada")
        
        print("Digite 2 para retornar a Tela Inicial")
        aux = int(input("Digite qual operação deseja realizar:"))
        print("")
        if aux == 1:
            print("############## INFORMAÇÕES DETALHADAS #################\n")
            print("*********************************************************\n")
            c = 0
            while c < NumdeCarros:
                print("{} - {} {} {} - Valor: R${},00 {}".format(Codigos[c], Marca[c], Modelo[c], Ano[c], Valor[c],
                                                             Status[c]))
                c = c + 1
                print("*********************************************************\n")
            print("======================================================\n")
        print("")
    if comando == 3:
        print("##### Alugar/Reservar Veículos ######")
        print("Digite 1 para ALUGAR o veículo.")
        print("Digite 2 para RESERVAR o veículo.")
        op = input("Digite a operação desejada:")
        print("")
        if op == "1":
            nl = input("Nome do locador:")
            prazo = int(input("Prazo de locação:"))
            if prazo > 30:
                print("Prazo muito grande.")
                prazo = input("Digite um prazo de locação menor:")
            cd = input("Código do Veículo:")
            if str(Status[int(cd)-1]) == "DISPONÍVEL":
                Prazo[int(cd)-1] = prazo
                Status[int(cd)-1] = "ALUGADO"
                Cliente[int(cd)-1] = nl
                Ialuguel[int(cd)-1] = str(str(Dia)+str(Mes)+str(Anos))
                d = Dia + prazo
                m = Mes
                a = Anos
                if d > 30:
                    d = d - 30
                    m = m + 1
                    if m > 12:
                        m = m - 12
                        a = a + 1
                Faluguel[int(cd) - 1] = str(str(d) + str(m) + str(a))
            elif str(Status[int(cd)-1]) == "ALUGADO":
                print("Esse veículo não pode ser alugado.")
                cd = input("Código de um outro veículo:")
                if str(Status[int(cd) - 1]) == "DISPONÍVEL":
                    Status[int(cd) - 1] = "ALUGADO"
                    Cliente[int(cd) - 1] = nl
                    Ialuguel[int(cd) - 1] = str(str(Dia) + str(Mes) + str(Anos))
                    d = Dia + prazo
                    m = Mes
                    a = Anos
                    if d > 30:
                        d = d - 30
                        m = m + 1
                        if m > 12:
                            m = m - 12
                            a = a + 1
                    Faluguel[int(cd) - 1] = str(str(d) + str(m) + str(a))
                if str(Status[int(cd) - 1]) == "RESERVADO":
                    print("Existe sobreposição de datas, Escolha outro carro ou outra data")
        elif op == "2":
            nl = input("Nome do locador:")
            prazo = int(input("Prazo de locação:"))
            if prazo > 30 - Dia:
                print("Prazo muito grande.")
                prazo = input("Digite um prazo de locação menor:")
            cd = input("Código do Veículo:")
            if str(Status[int(cd)-1]) == "DISPONÍVEL":
                Prazo[int(cd) - 1] = prazo
                Status[int(cd)-1] = "RESERVADO"
                Cliente[int(cd)-1] = nl
                ini = (input("Data do Início do aluguel sem / ex: 12012017 :"))
                d = int(ini[0] + ini[1])
                m = int(ini[2] + ini[3])
                a = int(ini[4] + ini[5] + ini[6] + ini[7])
                d = d + prazo
                if d > 30:
                    d = d - 30
                    m = m + 1
                    if m > 12:
                        m = m - 12
                        a = a + 1
                Faluguel[int(cd) - 1] = str(str(d) + str(m) + str(a))
        print("\n====================================\n")
    if comando == 4:
        print("######### Devolver/Liberar Veículos #########")
        print("\n***********************************")
        a = len(Codigos)
        b = 0
        while b < a:
            if Status[b] != "DISPONÍVEL":
                print(str(Codigos[b])+"--"+str(Modelo[b])+"--"+str(Status[b]))
                print("***********************************")
            b = b + 1
        print("\nDigite 1 para Devolver Veículo")
        print("Digite 2 para Liberar Veículo")
        res = int(input("Digite a opção desejada:"))
        print("")
        if res == 1:
            print("***********************************")
            cod = int(input("Digite o Código do Veículo:"))
            print("\nCliente: ", Cliente[cod - 1])
            val = int(Ialuguel[cod - 1])//1000000
            d = val
            m = (int(Ialuguel[cod - 1]) - d*1000000) // 10000
            a = (int(Ialuguel[cod - 1]) - d*1000000) % 10000
            if a == Anos:
                if m > Mes:
                    print("Total a pagar: R$", (((30-d)+Dia) * float(Valor[cod - 1])))
                    Status[cod - 1] = "DISPONÍVEL"
                elif m == Mes:
                    if Dia == d:
                        print("Total a pagar: R$", (float(Valor[cod - 1])))
                        Status[cod - 1] = "DISPONÍVEL"
                    elif Dia > d:
                        print("Total a pagar: R$", ((Dia - d) * float(Valor[cod - 1])))
                        Status[cod - 1] = "DISPONÍVEL"
                    elif d > Dia:
                        Status[cod - 1] = "DISPONÍVEL"
            elif a < Anos:
                print("Total a pagar: R$", ((Dia + (30 - d)) * float(Valor[cod - 1])))
                Status[cod - 1] = "DISPONÍVEL"
            elif a > Anos:
                Status[cod - 1] = "DISPONÍVEL"
        print("***********************************\n")
        print("================================================\n")
        if res == 2:
            cod = int(input("Digite o Código do Veículo:"))
            print("Cliente: ", Cliente[cod - 1])
            val = int(Ialuguel[cod - 1]) // 1000000
            d = val
            m = (int(Ialuguel[cod - 1]) - d * 1000000) // 10000
            a = (int(Ialuguel[cod - 1]) - d * 1000000) % 10000
            if a > Anos:
                Status[cod - 1] = "DISPONÍVEL"
            elif a < Anos:
                val = Dia + (30 - d)
                print("Total a pagar: R$", (val * float(Valor[cod - 1])))
                Status[cod - 1] = "DISPONÍVEL"
            elif a == Anos:
                if m == Mes:
                    if d == Dia:
                        print("Total a pagar: R$", (float(Valor[cod - 1])))
                        Status[cod - 1] = "DISPONÍVEL"
                    elif d > Dia:
                        Status[cod - 1] = "DISPONÍVEL"
                    else:
                        val = Dia - d
                        print("Total a pagar: R$", (val * float(Valor[cod - 1])))
                        Status[cod - 1] = "DISPONÍVEL"
    if comando == 5:
        print("########## EXCLUIR VEÍCULOS ###########\n")
        vei = int(input("Digite o Código do Veículo: "))
        if Status[vei - 1] == "DISPONÍVEL":
            del Codigos[vei - 1]
            del Marca[vei - 1]
            del Modelo[vei - 1]
            del Ano[vei - 1]
            del Valor[vei - 1]
            del Status[vei - 1]
            del Ialuguel[vei - 1]
            del Faluguel[vei - 1]
            del Cliente[vei - 1]
            del objetos[vei - 1]
        ve = len(Status)
        y = 1
        x = 0
        while x < ve:
            Codigos[x] = "00" + str(y)
            x = x + 1
    if comando == 6:
        Dia = Dia + 1
        if Dia > 30:
            Dia = Dia - 30
            Mes = Mes + 1
            if Mes > 12:
                Mes = Mes - 12
                Anos = Anos + 1
        cod = len(Status)
        while cod > 0:
            d = (int(Ialuguel[cod - 1])) // 1000000
            m = (int(Ialuguel[cod - 1]) - d * 1000000) // 10000
            a = (int(Ialuguel[cod - 1]) - d * 1000000) % 10000
            if Status[cod - 1] == "DISPONÍVEL":
                print()
            elif a == Anos:
                if m > Mes:
                    if ((30 - d) + Dia) > Prazo[cod - 1]:
                        Status[cod - 1] = "ATRASADO"
                elif m == Mes:
                    if Dia == d:
                        Status[cod - 1] = "ALUGADO"
                    elif Dia > d:
                        if (Dia - d) > Prazo[cod - 1]:
                            Status[cod - 1] = "ATRASADO"
            elif a < Anos:
                if (Dia + (30 - d)) > Prazo[cod - 1]:
                    Status[cod - 1] = "ATRASADO"
            cod = cod - 1
        print("")
        print("######### PASSOU UM DIA #######\n\n")
    if comando == 7:
        print("-------------- LOCALIZA AGRADECE A PREFERÊNCIA, VOLTE SEMPRE. --------------")
        break
