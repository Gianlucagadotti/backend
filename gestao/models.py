from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    def __str__ (self):
        return self.nome   
    
class Curso(models.Model):
    nome_curso = models.CharField(max_length=100) 
    carga_horaria = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__  (self):
        return f'{self.nome_curso} - {self.carga_horaria} horas'

class Matricula(models.Model):
    num_matricula = models.CharField(max_length=10)
    data_matricula = models.DateField()
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    def __str__ (self):
        return f'{self.num_matricula} - {self.aluno.nome} - {self.curso.nome_curso}'
    
class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=60)
    carga_horaria = models.DecimalField(max_digits=5, decimal_places=2)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __str__ (self):
        return f'{self.nome_disciplina} - {self.carga_horaria} horas'
    
class Professor(models.Model):
    nomeProf = models.CharField(max_length=100)
    emailProf = models.EmailField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    def __str__ (self):
        return f'{self.nomeProf} - {self.disciplina.nome_disciplina}'
    
class Turma(models.Model):
    ano_turma = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    
    def __str__ (self):
        return f'{self.ano_turma} - {self.professor.nomeProf} - {self.disciplina.nome_disciplina}'
    
class Frequencia(models.Model):
    presenca = models.CharField(max_length=100)
    
    def __str__ (self):
        return self.presenca