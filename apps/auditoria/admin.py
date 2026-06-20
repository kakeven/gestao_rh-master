#Sendo responsavel apenas para a exibição e gerenciar os dados no painel adm

#Importação da biblioteca do Django para painel Adminstrativo
#E tambem importação do model da Auditoria
from django.contrib import admin
from .models import LogAuditoria 

#Aqui foi colocado um atalho para nao registrar manualmente
#E como vai se comportar dentro do painel, Como colunas da tabela / Barra lateral de filtros / Campo de busca / E colocando como apenas leitura
@admin.register(LogAuditoria) 
class LogAuditoriaAdmin(admin.ModelAdmin): 
    list_display    = ('usuario', 'acao', 'descricao', 'data_hora') 
    list_filter     = ('acao',)                                     
    search_fields   = ('usuario__username', 'descricao')            
    readonly_fields = ('usuario', 'acao', 'descricao', 'data_hora')
    actions         = None 

#Aqui é para remover o botao padrao de adicionar do propio Django, para não adicionar logs, apenas receber
    def has_add_permission(self, request):
        return False