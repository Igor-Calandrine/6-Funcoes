"""Impressão de modelos: Coloque funções em um arquivo separado de nome. Escreva uma instrução import no início de e modifique o arquivo para usar as funções importadas."""

import modulo_015 as modulo

modulo.carros_garagem = []

modulo.carros_características("citroen", "c3", cor="cinza", câmbio="manual")
modulo.carros_características("pegeout", "208", cor="azul", câmbio="automático")
modulo.carros_características("wolks", "gol", cor="preto", câmbio="manual")
modulo.apresentar_carros(modulo.carros_garagem)