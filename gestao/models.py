from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    def __str__ (self):
        return self.nome   
    
class Curso(models.Model):
    nome_curso = models.CharField(max_length=100, default='Curso Genérico') 
    carga_horaria = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    def __str__  (self):
        return f'{self.nome_curso} - {self.carga_horaria} horas'

class Matricula(models.Model):
    num_matricula = models.CharField(max_length=10)
    data_matricula = models.DateField(max_length=12, default=None, null=True, blank=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, default=None, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, default=None, null=True, blank=True)
    def __str__ (self):
        return f'{self.num_matricula} - {self.aluno.nome} - {self.curso.nome_curso}'
    
class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=60, default='Disciplina Genérica')
    carga_horaria = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, default=None, null=True, blank=True)

    def __str__ (self):
        return f'{self.nome_disciplina} - {self.carga_horaria} horas'
    
class Professor(models.Model):
    nomeProf = models.CharField(max_length=100)
    emailProf = models.EmailField(max_length=320, default=None, null=True, blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, default=None, null=True, blank=True)
    def __str__ (self):
        return f'{self.nomeProf} - {self.disciplina.nome_disciplina}'
    
class Turma(models.Model):
    ano_turma = models.CharField(max_length=50, default='2025')
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, default=None, null=True, blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, default=None, null=True, blank=True)
    
    def __str__ (self):
        return f'{self.ano_turma} - {self.professor.nomeProf} - {self.disciplina.nome_disciplina}'
    
class Frequencia(models.Model):
    presenca = models.CharField(max_length=100)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, default=None, null=True, blank=True)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, default=None, null=True, blank=True)
    data_frequencia = models.DateField(max_length=12, default=None, null=True, blank=True)
    def __str__ (self):
        return f'{self.presenca} - {self.aluno} - {self.turma} - {self.data_frequencia}'