import random 

class Jogador:
    def __init__(self, idd, hab, luck):
        self.id = idd
        self.hab = hab
        self.luck = luck
        self.total = hab+luck

    def get_total(self):
        return self.total



class Lista:
    def __init__(self, n_total):
        self.list = []
        for count in range(n_total):
            l_hab = random.randint(0, 950)
            l_luck = random.randint(0, 50)
            self.list.append(Jogador(count,l_hab,l_luck))

    
qtd = 100000
teste = Lista(qtd)
order = sorted(teste.list, key=Jogador.get_total, reverse=True)

f = open("teste.txt","a")

for count in range(qtd):
    f.write(f"\n Posição: °{count+1}     ID: {order[count].id}      Hab: {order[count].hab}      Luck: {order[count].luck}      Total: {order[count].total}")

f.close()