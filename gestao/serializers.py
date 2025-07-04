from rest_framework.serializers import ModelSerializer
from .models import Aluno, Curso, Matricula, Disciplina, Professor, Turma, Frequencia

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
class MatriculaSerializer(ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
class DisciplinaSerializer(ModelSerializer):    
    class Meta:
        model = Disciplina
        fields = '__all__'
class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
class FrequenciaSerializer(ModelSerializer):
    class Meta:
        model = Frequencia
        fields = '__all__'       