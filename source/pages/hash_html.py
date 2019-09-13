# -*- coding: utf-8 -*-


class HashHtml:

    @classmethod
    def __init__(cls, senha, lvl, md5):
        cls.html=\
                """
                <html>
                    <head>
                        <title>Gera Senha e Hash</title>
                    </head>
                    <body>
                    	<p style = "font-family:arial;font-size:35px;font-style:italic;color:#66d9ff;text-align:center">
                          Senha: {}
                      </p>
                      <p style = "color:#ff668c;font-size:24px;text-align:center;">
                        Nivel: {}
                      </p>
                      <p style = "color:#66ff66;font-size:24px;text-align:center;">
                        Hash MD5: {}
                      </p>

                    </body>
                </html>             
                """.format(senha, lvl, md5)

