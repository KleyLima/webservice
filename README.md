# webservice

Implementação de um pequeno webservice tendo como serviços outros scripts desenvolvidos.

A porta liberada para os endpoints é a 7979 que pode ser acessada por http://localhost:7979/
A porta pode ser modificada no código.

Os endpoints desenvolvidos são:

 - conversão de números romanos no endpoint ./romano/{numero}
      onde a resposta deve ser o número em algarismos romanos

  - validação de cpf's no endpoint ./valida_cpf/{cpf}
      onde a resposta deve ser o cpf e sua classificação (válido/inválido)

  - distancia de zeros no endpoint ./dist_zeros/{string}
      onde a resposta deve ser a string e a maior quantidade de zeros consecutivos

  - gerador de senhas + classificador de senhas + hash no endpoint ./gera_senha/
      onde a resposta deve ser a senha gerada, sua classificação e o hash calculado


