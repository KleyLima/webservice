# -*- coding: utf-8 -*-


class RomanHtml:

    @classmethod
    def __init__(cls, number):
        cls.html=\
                """
                <html>
	            <head>
		        <title>Roman Converter</title>
	            </head>

	            <body>
		        <p style = "font-family:arial;font-size:20px;font-style:italic;color:red;text-align:center">
		        {}
		        </p>
	            </body>
                </html>               
                """.format(number)

