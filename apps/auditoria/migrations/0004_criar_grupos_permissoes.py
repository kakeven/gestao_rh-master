#Aqui é onde fica responsavel por ajeitar criar os grupos de permissões

#Importamos a biblioteca de migrations pra criar e executar migrações no banco
from django.db import migrations

#Função onde cria 3 tipos de grupos com as permisões especificas
#Acessamos o model de grupos e de permissoes
def criar_grupos(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

#Aqui buscamos as 4 permissões automaticas de uma model, onde pegamos
#o nome do app e do model 
    def get_perms(app, model):
        return Permission.objects.filter(
            content_type__app_label=app,
            content_type__model=model
        )

    #GERENTE DE RH
    #Criamos o grupo de permissões para o Gerente de RH e colocamos quais vai ser as permissões
    #Recebendo o CRUD completo
    gerente, _ = Group.objects.get_or_create(name='Gerente de RH')
    gerente.permissions.set([
        *get_perms('funcionarios', 'funcionarios'),
        *get_perms('departamentos', 'departamento'),
        *get_perms('empresa', 'empresa'),
        *get_perms('documentos', 'documento'),
        *get_perms('registro_hora_extra', 'registrohoraextra'),
        *get_perms('auditoria', 'logauditoria'),
        *get_perms('auth', 'user'),
    ])

    #ADMINISTRADOR DO SISTEMA
    admin, _ = Group.objects.get_or_create(name='Administrador do Sistema')
    admin.permissions.set(Permission.objects.all())

    #FUNCIONÁRIO DE RH
    funcionario, _ = Group.objects.get_or_create(name='Funcionário de RH')
    funcionario.permissions.set([
        *get_perms('documentos', 'documento'),
        *get_perms('registro_hora_extra', 'registrohoraextra'),
    ])

#Classe migration onde roda apos a dependecia e executa a função criar grupos ao rodar migrate
class Migration(migrations.Migration):

    dependencies = [
        ('auditoria', '0003_alter_logauditoria_acao'),
    ]

    operations = [
        migrations.RunPython(criar_grupos, migrations.RunPython.noop),
    ]