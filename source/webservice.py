# -*- coding: utf-8 -*-

from aiohttp import web
from handler.converte_romano_kleyton import Roman
from handler.validacpf_kleyton import ValidaCPF
from handler.conta_zero_kleyton import ContaZero
from handler.hash_senha import HashSenha
from handler.classifica_senha import ClassificaSenha
from handler.gera_senha_kleyton import GeraSenha

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
        return web.Response(text = "{}\n".format(Roman(numero).numero_para_romano()))

    async def valida_cpf(self, request):
        cpf = request.match_info['cpf']
        return web.Response(text = "{}\n{}\n".format(cpf, ValidaCPF(cpf).valida_cpf()))

    async def dist_zeros(self, request):
        string = request.match_info['string']
        return web.Response(text = "{}\n{}\n".format(string, ContaZero(string).conta_zeros()))

    async def gera_senha(self, request):
        senha = GeraSenha().gera_senha()
        lvl = ClassificaSenha(senha).classifica_senha()
        cript = HashSenha(senha) 
        md5 = cript.hash_md5()
        return web.Response(text = "{}\n{}\n{}\n".format(senha, lvl, md5))
      

if __name__ == '__main__':
    handler = Handler()

