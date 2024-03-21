class Elemento:
    def __init__(self, nome:str, nota:float):
        self.nome = nome
        self.nota = nota
        self.proximo = None

class Lista:
    def __init__(self):
        self.primeiro = None
    
    def inserir_inicio(self, nome, nota):
        novo_elemento = Elemento(nome, nota)
        if self.primeiro is None:
            self.primeiro = novo_elemento
        else:
            novo_elemento.proximo = self.primeiro
            self.primeiro = novo_elemento
    
    def inserir_fim(self, nome, nota):
        novo_elemento = Elemento(nome, nota)
        if self.primeiro is None:
            self.primeiro = novo_elemento
        else:
            atual = self.primeiro
            while True:
                if atual.proximo is None:
                    atual.proximo = novo_elemento
                    break
                else:
                    atual = atual.proximo
    
    def imprimir_elementos(self):
        if self.primeiro is None:
            print('A lista esta vazia!')
        else:
            atual = self.primeiro
            while atual:
                print(f"Nome: {atual.nome}, Nota: {atual.nota}")
                atual = atual.proximo
    def verifica_vazia(self):
        if self.primeiro is None:
            print('A lista esta vazia!')
        else:
            print('A lista nao esta vazia')

    def buscar_elemento(self, elemento):
        atual = self.primeiro
        while atual:
            if atual.nome == elemento:
                print(f"Elemento Encontrado. Nome: {atual.nome}, Nota: {atual.nota}")
                break
            atual = atual.proximo

    def retirar_elemento(self, elemento):
        atual = self.primeiro
        while atual:
            if atual.nome == elemento:
                print(f"Elemento {elemento} removido.")
                self.primeiro = atual.proximo
                break
            else:
                if atual.proximo.nome == elemento:
                    print(f"Elemento {elemento} removido.")
                    atual.proximo = atual.proximo.proximo
                    break
                else:
                    atual = atual.proximo
    
    def esvaziar_lista(self):
        self.primeiro = None

lista = Lista()

lista.inserir_inicio('jose', 5.50)
lista.inserir_inicio('felipe', 7.50)
lista.inserir_fim('maria', 8.50)

# lista.imprimir_elementos()
# lista.retirar_elemento('jose')
# lista.imprimir_elementos()
# lista.esvaziar_lista()
# lista.imprimir_elementos()
