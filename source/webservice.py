# -*- coding: utf-8 -*-

from aiohttp import web
from handler.converte_romano_kleyton import Roman
from handler.validacpf_kleyton import ValidaCPF
from handler.conta_zero_kleyton import ContaZero
from handler.hash_senha import HashSenha
from handler.classifica_senha import ClassificaSenha
from handler.gera_senha_kleyton import GeraSenha
from pages.roman_html import RomanHtml
from pages.cpf_html import CPFHtml
from pages.dist_html import DistHtml
from pages.hash_html import HashHtml
from jinja2 import Environment, PackageLoader, select_autoescape
from os import system

class Handler:
    """
    Classe que representa os endpoints expostos no serviço, suas respectivas funções de tratamento e parâmetros que
    são passados na chamada.
    """
    def __init__(self):
        """Método que executa ao instanciar a classe, carrega os endpoints na tabela de rota e inicializa o serviço no port 7979"""
        app = web.Application()
        app.add_routes([web.get('/', self.home_page),
            web.get('/romano/{numero}', self.get_romano),
            web.get('/valida_cpf/{cpf}', self.valida_cpf),
            web.get('/dist_zeros/{string}', self.dist_zeros),
            web.get('/gera_senha', self.gera_senha)])
        app.router.add_static('/pages/', path='pages/', append_version = False)  # Adiciona rota 'interna' para arquivos dentro do projeto.
        web.run_app(app, host = 'localhost', port = 7979)
   
    async def get_romano(self, request):
        """ Método do endpoint de números romanos, chama a função e exibe o resultado formatado com HTML"""
        numero = request.match_info['numero']
        return web.Response(text = RomanHtml(Roman(numero).numero_para_romano()).html, content_type = 'http')

    async def valida_cpf(self, request):
        """ Método do endpoint do validador de CPF, chama a função e exibe o resultado formatado com HTML"""
        cpf = request.match_info['cpf']
        return web.Response(text = CPFHtml(cpf, ValidaCPF(cpf).valida_cpf()).html, content_type = 'http')

    async def dist_zeros(self, request):
        """ Método do endpoint de distancia de zeros, chama a função e exibe o resultado formatado com HTML"""
        string = request.match_info['string']
        return web.Response(text = DistHtml(string, ContaZero(string).conta_zeros()).html, content_type = 'html')

    async def gera_senha(self, request):
        """ Método do endpoint do gerador de senhas, chama a função e exibe o resultado formatado com HTML"""
        senha = GeraSenha().gera_senha()
        lvl = ClassificaSenha(senha).classifica_senha()
        cript = HashSenha(senha) 
        md5 = cript.hash_md5()
        return web.Response(text = HashHtml(senha, lvl, md5).html, content_type = 'html')
    
    async def home_page(self, request):
        """ Método da homepage do serviço."""
        env = Environment(
                loader = PackageLoader('webservice','pages'),  # Mapeia a pasta webservice/pages/
                autoescape = select_autoescape(['html']))      # Seleciona tipo de arquivo
        page = env.get_template('index.html')                  # Seleciona o arquivo da página
        out = page.render()                                    # Renderiza o modelo
        return web.Response(text = out, content_type = 'html')


if __name__ == '__main__':
    system('firefox localhost:7979')
    handler = Handler()
