#Aqui é responsavel por customizar o painel admin para o model de Usuarios do Django

#Importamos bibliotecas do Django para campo de formulario
#Pegamos as models User e Group, e usamos o UserAdmin para poder customizar nossos campos
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

#Aqui colocamos uma restrição para selecionar apenas um grupo, ai o metodo é chamado quando o forms é salvo
#Pega o valor selecionado que é unico e converte em uma lista
class SingleGroupWidget(forms.RadioSelect):
    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        return [value] if value else []


class CustomUserAdmin(UserAdmin):

    #Nessa função fica quais seções e campos aparecem no formulario
    #E verificamos se deve ou nao aparecer permissões individuais 
    def get_fieldsets(self, request, obj=None):
        if not request.user.is_superuser and obj is not None:
            return (
                (None, {'fields': ('username', 'password')}),
                ('Informações pessoais', {'fields': ('first_name', 'last_name', 'email')}),
                ('Permissões', {'fields': ('is_active', 'is_staff', 'groups')}),
                ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
            )
        return super().get_fieldsets(request, obj)

    #Aqui serve apenas para o campo grupos
    #Onde esconde o grupo Administrador do Sistema para não superusuarios
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'groups':
            queryset = Group.objects.all()
            if not request.user.is_superuser:
                queryset = queryset.exclude(name='Administrador do Sistema')
            kwargs['queryset'] = queryset
            kwargs['widget'] = SingleGroupWidget
        return super().formfield_for_manytomany(db_field, request, **kwargs)

#Logo aqui se remove o User padrão do Admin e deixa customizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)