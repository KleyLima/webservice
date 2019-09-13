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

class Handler:
    def __init__(self):
        app = web.Application()
        app.add_routes([web.get('/romano/{numero}', self.get_romano),
            web.get('/valida_cpf/{cpf}', self.valida_cpf),
            web.get('/dist_zeros/{string}', self.dist_zeros),
            web.get('/gera_senha', self.gera_senha)])
        web.run_app(app, host = 'localhost', port = 7979)

   
    async def get_romano(self, request):
        numero = request.match_info['numero']
        return web.Response(text = RomanHtml(Roman(numero).numero_para_romano()).html, content_type = 'http')

   async def valida_cpf(self, request):
        cpf = request.match_info['cpf']
        return web.Response(text = CPFHtml(cpf, ValidaCPF(cpf).valida_cpf()).html, content_type = 'http')

    async def dist_zeros(self, request):
        string = request.match_info['string']
        return web.Response(text = DistHtml(string, ContaZero(string).conta_zeros()).html, content_type = 'html')

    async def gera_senha(self, request):
        senha = GeraSenha().gera_senha()
        lvl = ClassificaSenha(senha).classifica_senha()
        cript = HashSenha(senha) 
        md5 = cript.hash_md5()
        return web.Response(text = HashHtml(senha, lvl, md5).html, content_type = 'html')
      
 

if __name__ == '__main__':
    handler = Handler()

