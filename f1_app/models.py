from django.db import models

# Definição do modelo de Equipes Fórmula 1.
class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=50)
    pais = models.CharField(max_length=20) 

    def __str__(self):
        # Retorno de uma representação de string
        return f'Nome da equipe: {self.nome_equipe}, País: {self.pais}'

# Definição do modelo Pilotos de Fórmula 1
class Pilotos(models.Model):
    equipe = models.ForeignKey(Equipe, related_name='piloto_equipe', on_delete=models.CASCADE)
    
    
    nome_do_primeiro_piloto = models.CharField(max_length=50) 
    numero_do_carro_1 = models.IntegerField()
    
    nome_do_segundo_piloto = models.CharField(max_length=50)
    numero_do_carro_2 = models.IntegerField()

    def __str__(self):
        # Retorno de uma representação de string 
        return f'Equipe: {self.equipe}, Nome do primeiro piloto: {self.nome_do_primeiro_piloto}, Número do carro: {self.numero_do_carro_1}, Nome do segundo piloto: {self.nome_do_segundo_piloto}, Número do carro: {self.numero_do_carro_2}'
