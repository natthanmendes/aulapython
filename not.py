class Aluno:
    def __init__(self,nome, nota, aprovado):
        self.nome = nome
        self._nota = nota
        self._aprovado = aprovado

        @property
        def nota(self):
            return self._nota

        @nota.setter
        def nota(self,nota):
            if nota < 0 or nota > 10:
                raise ValueError("A nota deve estar entre 0 e 10")
            self._nota = nota

        @property
        def aprovado(self):
            return self.nota >= 7

a = Aluno("Nathan", 8,)

print(a.nome)
print(a._nota)
print(a._aprovado)

a.nota = 9