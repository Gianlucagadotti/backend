from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Aluno, Curso, Matricula, Disciplina, Professor, Turma, Frequencia
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer, DisciplinaSerializer, ProfessorSerializer, TurmaSerializer, FrequenciaSerializer

class alunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class cursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class matriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class disciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class professorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class turmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class frequenciaViewSet(ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer
# Create your views here.
