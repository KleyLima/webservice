# -*- coding: utf-8 -*-

from aiohttp import web
from roman_converter.source.converte_romano_kleyton import Roman
from valida_cpf.source.validacpf_kleyton import ValidaCPF

class Handler:
    def __init__(self):
        app = web.Application()
        app.add_routes([web.get('/romano/{numero}', self.get_romano)])
        web.run_app(app, port = 7979)

    async def get_romano(self, request):
        numero = request.match_info['numero']
        return web.Response(
                text = "{}".format(Roman(numero).numero_para_romano()))

if __name__ == '__main__':
    handler = Handler()
# TESTE
# for x in str(system('curl localhost:7979/romano/99')):
#   print(x[:-1])

