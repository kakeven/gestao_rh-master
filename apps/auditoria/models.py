#É onde fica a estrutura do banco, definição das tabelas e colunas

#Aqui pegamos a biblioteca do Django para criar as tabelas no banco.
#E tambem a tabela de usuarios, que o propio Django disponibiliza.

from django.db import models
from django.contrib.auth.models import User

#Nessa classe é a tabela que armazena os logs de auditoria.
#E temos a nossa lista de opções para o campo de ação, 
#onde o temos o CREATE é oque salva no banco e a Criação é oque aparece para nosso usuario.

class LogAuditoria(models.Model):
    ACAO_CHOICES = [              
        ('CREATE', 'Criação'),    
        ('UPDATE', 'Atualização'),
        ('DELETE', 'Exclusão'),
    ]
#Aqui temos as colunas da nossa tabela
#Onde liga o log ao usuario que fez ação / Qual foi o tipo de ação / A descrição do que aconteceu / Salvamento da data e hora que o log foi criado
    usuario   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    acao      = models.CharField(max_length=10, choices=ACAO_CHOICES)         
    descricao = models.TextField()                                            
    data_hora = models.DateTimeField(auto_now_add=True)                       

#Aqui temos configurações da ordem da lista(sendo do mais recente para o mais antigo)
    class Meta:       
        ordering = ['-data_hora']                   
        verbose_name = 'Log de Auditoria'           
        verbose_name_plural = 'Logs de Auditoria'   

#Aqui é mais como o objeto aparece quando exibido como texto quando lista os logs
    def __str__(self):
        return f'{self.usuario} - {self.acao} - {self.data_hora}' 