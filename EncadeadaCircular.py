class Elemento:
    def __init__(self, nome:str, nota:float):
        self.nome = nome
        self.nota = nota
        self.proximo = None
        self.anterior = None

class Lista:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.cursor = None

    def adicionarInicio(self, nome, nota):
        novo_elemento = Elemento(nome, nota)
        if self.primeiro is None:
            self.primeiro = novo_elemento
            self.ultimo = novo_elemento
            self.cursor = novo_elemento
            novo_elemento.proximo = novo_elemento
            novo_elemento.anterior = novo_elemento
        else:
            novo_elemento.proximo = self.primeiro
            self.primeiro.anterior = novo_elemento
            self.primeiro = novo_elemento
            self.cursor = novo_elemento
            self.ultimo.proximo = novo_elemento
            self.primeiro.anterior = self.ultimo


    def adicionarFim(self, nome, nota):
        novo_elemento = Elemento(nome, nota)
        if self.primeiro is None:
            self.primeiro = novo_elemento
            self.ultimo = novo_elemento
            self.cursor = novo_elemento
            novo_elemento.proximo = novo_elemento
            novo_elemento.anterior = novo_elemento
        else:
            novo_elemento.proximo = self.primeiro
            self.primeiro.anterior = novo_elemento
            self.ultimo.proximo = novo_elemento
            novo_elemento.anterior = self.ultimo
            self.ultimo = novo_elemento
            self.cursor = novo_elemento

    def imprimir_normal(self):
        if self.primeiro is None:
            print('A lista está vazia')
        else:
            atual = self.primeiro
            print(f"Nome: {atual.nome}, Nota: {atual.nota}")
            atual = atual.proximo
            while atual != self.primeiro:
                print(f"Nome: {atual.nome}, Nota: {atual.nota}")
                atual = atual.proximo
                
    def imprimir_inverso(self):
        if self.primeiro is None:
            print('A lista está vazia')
        else:
            atual = self.ultimo
            while True:
                if atual == self.primeiro:
                    print(f"Nome: {atual.nome}, Nota: {atual.nota}")
                    break
                else:
                    print(f"Nome: {atual.nome}, Nota: {atual.nota}")
                    atual = atual.anterior

    def listaVazia(self):
        return self.primeiro is None

    def buscarElemento(self, elemento:str):
        atual = self.primeiro
        while atual:
            if atual.nome == elemento:
                print(f"Nome: {atual.nome}, Nota: {atual.nota}")
                return
            atual = atual.proximo
        print("Elemento não encontrado.")

    def eliminarElemento(self, elemento:str):
        atual = self.primeiro
        while atual:
            if atual.nome == elemento:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.primeiro = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.ultimo = atual.anterior
                print(f"Elemento '{elemento}' removido com sucesso.")
                return
            atual = atual.proximo
        print("Elemento não encontrado.")

    def esvaziarLista(self):
        self.primeiro = None 
        self.ultimo = None 
        self.cursor = None

#ADICIONAIS =====================
    def inserir_vetor(self, vetor):
        for nome, nota in vetor:
            self.adicionarFim(nome, nota)


    def transformar_vetor(self):
        vetor = []
        if self.primeiro is None:
            print('A lista está vazia')
        else:
            atual = self.primeiro
            while atual:
                elemento = []
                elemento.append(atual.nome)
                elemento.append(atual.nota)
                vetor.append(elemento)
                atual = atual.proximo
        print(vetor)
    def numero_nos(self):
        contador = 0
        atual = self.primeiro
        while atual:
            contador += 1
            atual = atual.proximo
        print(contador)

lista = Lista()

lista.adicionarInicio("Joao", 8.5)
lista.adicionarInicio("Maria", 9.0)
lista.adicionarInicio("Carlos", 7.8)
lista.adicionarFim("Jose", 7.8)
# print("Lista antes da remocao:")
lista.imprimir_normal()
print()
lista.eliminarElemento("Maria")
lista.imprimir_normal()
print()
lista.imprimir_inverso()
# print("\nLista apos a remocao:")
# lista.imprimir()
