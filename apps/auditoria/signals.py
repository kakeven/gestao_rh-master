#Aqui são os gatilhos automaticos, fica escutando o banco e quando acontece uma ação ele dispara automaticamente e grava o log na tabela

#Nessa bloco é a parte onde o sinal dispara ao salvar (criar/editar) ou deletar e tambem o responsavel por escutar o sinal
#Importamos todos os models que vai ser monitorados para mandar os logs
#E tambem o responsavel do middleare para saber a pessoa que ta logada
from django.db.models.signals import post_save, post_delete 
from django.dispatch import receiver                        
from apps.funcionarios.models import Funcionarios           
from apps.departamentos.models import Departamento
from apps.documentos.models import Documento
from apps.empresa.models import Empresa
from apps.registro_hora_extra.models import RegistroHoraExtra
from .models import LogAuditoria
from .middleware import get_current_user                    

#Nessa parte dos FUNCIONÁRIOS, temos os paramentros responsaveis por,
#escutar apenas a model especifica, saber qual model disparou o sinal, o objeto que foi salvo,
#recebimento de parametros especificos, saber o usuario logado e as regras da função especifica

@receiver(post_save, sender=Funcionarios)                       
def log_funcionario_save(sender, instance, created, **kwargs):
    LogAuditoria.objects.create(
        usuario=get_current_user(),                             
        acao='CREATE' if created else 'UPDATE',
        descricao=f'Funcionário "{instance}" criado.' if created else f'Funcionário "{instance}" atualizado.',
    )

@receiver(post_delete, sender=Funcionarios)
def log_funcionario_delete(sender, instance, **kwargs):
    LogAuditoria.objects.create(
        usuario=get_current_user(),
        acao='DELETE',
        descricao=f'Funcionário "{instance}" removido.',
    )

#DEPARTAMENTOS

@receiver(post_save, sender=Departamento)
def log_departamento_save(sender, instance, created, **kwargs):
    LogAuditoria.objects.create(
        usuario=get_current_user(),
        acao='CREATE' if created else 'UPDATE',
        descricao=f'Departamento "{instance}" criado.' if created else f'Departamento "{instance}" atualizado.',
    )

@receiver(post_delete, sender=Departamento)
def log_departamento_delete(sender, instance, **kwargs):
    LogAuditoria.objects.create(
        usuario=get_current_user(),
        acao='DELETE',
        descricao=f'Departamento "{instance}" removido.',
    )

#DOCUMENTOS

@receiver(post_save, sender=Documento)
def log_documento_save(sender, instance, created, **kwargs):
    LogAuditoria.objects.create(
        usuario=get_current_user(),
        acao='CREATE' if created else 'UPDATE',
        descricao=f'Documento "{instance}" criado.' if created else f'Documento "{instance}" atualizado.',
    )

@receiver(post_delete, sender=Documento)
def log_documento_delete(sender, instance, **kwargs):
    LogAuditoria.objects.create(
        usuario=get_current_user(),
        acao='DELETE',
        descricao=f'Documento "{instance}" removido.',
    )

#EMPRESA

@receiver(post_save, sender=Empresa)
def log_empresa_save(sender, instance, created, **kwargs):
    LogAuditoria.objects.create(
        usuario=get_current_user(),
        acao='CREATE' if created else 'UPDATE',
        descricao=f'Empresa "{instance}" criada.' if created else f'Empresa "{instance}" atualizada.',
    )

@receiver(post_delete, sender=Empresa)
def log_empresa_delete(sender, instance, **kwargs):
    LogAuditoria.objects.create(
        usuario=get_current_user(),
        acao='DELETE',
        descricao=f'Empresa "{instance}" removida.',
    )

#REGISTRO HORA EXTRA

@receiver(post_save, sender=RegistroHoraExtra)
def log_hora_extra_save(sender, instance, created, **kwargs):
    LogAuditoria.objects.create(
        usuario=get_current_user(),
        acao='CREATE' if created else 'UPDATE',
        descricao=f'Hora extra "{instance}" criada.' if created else f'Hora extra "{instance}" atualizada.',
    )

@receiver(post_delete, sender=RegistroHoraExtra)
def log_hora_extra_delete(sender, instance, **kwargs):
    LogAuditoria.objects.create(
        usuario=get_current_user(),
        acao='DELETE',
        descricao=f'Hora extra "{instance}" removida.',
    )