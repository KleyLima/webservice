# -*- coding: utf-8 -*-

from aiohttp import web
import atexit

async def test(request):
    return web.Response(text = "Teste")

def cria_endpoint():
    app = web.Application()
    app.add_routes([web.get('/', test)])
    web.run_app(app, port = 7979)

async def close():
    await WebSession.close()


def exit_handler():
    print("Saindo")
    close()

#atexit.register(exit_handler)

if __name__ == '__main__':
    cria_endpoint()
    #atexit.register(exit_handler)

