#Aqui é onde fica para intercepitar as requisições, para passar pro signals

#Importamos a biblioteca para guardar os dados separados do usuario
import threading    

#Foi feito a criação do espaço separado para cada requisição
_user = threading.local()   

#Função pra chamar pra saber que é que ta logado
def get_current_user():
    return getattr(_user, 'value', None)    

#Aqui foi feito a estrutura padrão do middleware no Django
#E pra que possamos passar a requisição pro proximo passo no sistema
class CurrentUserMiddleware:                
    def __init__(self, get_response):       
        self.get_response = get_response

#Aqui é responsavel por salvar o usuario logado e para que retorna a resposta da requisição normal
    def __call__(self, request):
        _user.value = request.user              #Salva o usuário logado no _user.value
        response = self.get_response(request)   #Deixa a requisição continuar normalmente
        return response                         #Retorna a resposta