class Commit:
    def __init__(self, id, mensagem, autor, pai=None):
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    def historico(self):
        print(f"#{self.id} {self.mensagem} ({self.autor})")
        
        if self.pai is None:
            return

        self.pai.historico()


class Repositorio:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador_commits = 0

    def commitar(self, mensagem):
        self.contador_commits += 1
        novo_commit = Commit(self.contador_commits, mensagem, self.autor, self.head)
        self.head = novo_commit

    def log(self):
        if self.head is None:
            print("Nenhum commit ainda")
            return

        self.head.historico()

    def total_de_commits(self):
        total = 0
        atual = self.head
        
        while atual is not None:
            total += 1
            atual = atual.pai
            
        return total


repositorio = Repositorio("meu-projeto", "Dani - 6326262")

repositorio.log()

repositorio.commitar("Cria o projeto")
repositorio.commitar("Adiciona o README")
repositorio.commitar("Corrige o titulo do README")

repositorio.log()

print(repositorio.total_de_commits())