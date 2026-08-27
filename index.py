# classe para salvar o livro e identificar se ele está disponível.
class Livro:
    def __init__(self, titulo, id):
        self.titulo = titulo
        self.id = id
        self.disponivel = True

    def mostrar(self):
        if self.disponivel:
            return "LIVRO DISPONÍVEL"
        else:
            return "LIVRO INDISPONÍVEL"


class Biblioteca:
    def __init__(self):#criei uma lista para armazenar os livros no catalogo
        self.catalogo = [] # lista vazia para adicionar os livros dinâmicamente

    def adicionar(self, livro):# adicionar livro usando o append()
        self.catalogo.append(livro)
        print(f"LIVRO:{livro.titulo} ADICIONADO COM SUCESSO!")
    def remover(self,titulo,id):#remover livro usando o remove()
        for livro in self.catalogo:#pecorre o catalogo
            if livro.titulo.lower()== titulo.lower() and livro.id==id:
                self.catalogo.remove(livro)
                print(f"livro: {livro.titulo} com id: {livro.id} removido com sucesso")
                return
        print(f"***[ERRO]*** LIVRO: {titulo} NÃO EXISTE NO CATÁLOGO OU OS DADOS DIGITADOS ESTÃO INCORRETOS")

    def listar(self):
        if not self.catalogo:
            print("CATÁLOGO VAZIO")
            return
        print("="*3, "CATÁLOGO DA BIBLIOTECA", "="*3)
        for i,livro in enumerate(self.catalogo,1):#utilizo o (for) para pecorer e ver se em self.catalogo tem livro e se tiver ele vai mostrar
            status=livro.mostrar() # variavel para mostrar o status do livro de acordo com a class Livro no metodo mostrar()
            print(f"{i}- O LIVRO: {livro.titulo} com ID: {livro.id} |STATUS: {status}")
    def emprestar(self,titulo):
        for livro in self.catalogo:
            if livro.titulo.upper() == titulo.upper():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"VOCE PEGOU O LIVRO:{livro.titulo} EMPRESTADO!")
                    return
                else:
                    print(f"livro: {livro.titulo} já esta emprestado")
                    return
        print(f"**[ERRO]** LIVRO {titulo} NÃO EXISTE NO CATÁLOGO OU DADOS DIGITADOS ESTÃO INCORRETOS")
    def devolver(self, id):
        for livro in self.catalogo:
            if livro.id==id:
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"LIVRO: {livro.titulo} DEVOLVIDO COM SUCESSO!")
                else:
                    print(f"LIVRO: {livro.titulo} JÁ FOI DEVOLVIDO ")
fluxo=Biblioteca() #objeto que faz ligação com a classe biblioteca

while True:
    print("="*20)
    print("GERENCIAMENTO DE LIVROS")
    print("="*20)

    print("========MENU========")
    print("1 - ADICIONAR LIVRO")
    print("2 - LISTAR LIVROS")
    print("3 - PEGAR EMPRESTADO")
    print("4 - DEVOLVER LIVRO")
    print("5- REMOVER LIVRO")
    print("0 - SAIR DO PROGRAMA")
    print("="*21)
    opcao = int(input("ESCOLHA UMA OPÇÃO: "))

    match opcao:
        case 1:
            nome=input("DIGITE O TITULO DO LIVRO PARA ADICIONAR AO CATALOGO: ").upper()
            ide=input("DIGITE A ID DO LIVRO: ")
            livro=Livro(nome,ide)
            fluxo.adicionar(livro)
        case 2:
            fluxo.listar()
        case 3:
            titulo=input("digite o titulo do livro para pegar emprestado: ").upper()
            fluxo.emprestar(titulo)
        case 4:
            devolucao=input("digite o id do livro para devolver: ")
            fluxo.devolver(devolucao)
        case 5:
            nome=input("DIGITE O TITULO QUE DESEJA REMOVER: ")
            ide=input("DIGITE A ID DO LIVRO QUE DESEJA REMOVER: ")
            fluxo.remover(nome,ide)
        case 0:
            print("SAINDO DO PROGRAMA")
            break
        case _:
            print("***[ERRO]*** DIGITE UM NUMERO VÁLIDO, TENTE NOVAMENTE.")