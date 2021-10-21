from unittest import TestCase
from base.componentes_graficos import Candlestick


class CandlestickTestes(TestCase):
    def teste_criacao_objeto(self):
        # inicializando a vela
        vela = Candlestick(1)
        self.assertEqual(1, vela.ponto_de_abertura)
        self.assertEqual(None, vela.ponto_de_fechamento)
        self.assertEqual(1, vela._ponto_de_minima)
        self.assertEqual(1, vela.ponto_de_maxima)
        self.assertEqual(1, vela.ponto_atual)
        self.assertEqual(Candlestick.status_vela_em_formacao, vela.status_da_vela)
        self.assertEqual(Candlestick.tipo_vela_neutra, vela.tipo_de_vela)

    def teste_variacao_pontos(self):
        vela = Candlestick(0)

        vela.ponto_atual = 56
        self.assertEqual(56, vela.ponto_de_maxima)
        self.assertEqual(0, vela.ponto_de_minima)
        self.assertEqual(Candlestick.tipo_vela_de_alta, vela.tipo_de_vela)
        self.assertEqual(Candlestick.status_vela_em_formacao, vela.status_da_vela)

        vela.ponto_atual = -200
        self.assertEqual(56, vela.ponto_de_maxima)
        self.assertEqual(-200, vela.ponto_de_minima)
        self.assertEqual(Candlestick.tipo_vela_de_baixa, vela.tipo_de_vela)
        self.assertEqual(Candlestick.status_vela_em_formacao, vela.status_da_vela)

        vela.ponto_atual = 500
        self.assertEqual(500, vela.ponto_de_maxima)
        self.assertEqual(-200, vela.ponto_de_minima)
        self.assertEqual(Candlestick.tipo_vela_de_alta, vela.tipo_de_vela)
        self.assertEqual(Candlestick.status_vela_em_formacao, vela.status_da_vela)

        vela.ponto_de_fechamento = 400
        self.assertEqual(500, vela.ponto_de_maxima)
        self.assertEqual(-200, vela.ponto_de_minima)
        self.assertEqual(Candlestick.tipo_vela_de_alta, vela.tipo_de_vela)
        self.assertEqual(Candlestick.status_vela_finalizado, vela.status_da_vela)
        self.assertEqual(vela.ponto_de_fechamento, vela.ponto_atual)

        vela.ponto_atual = 200
        self.assertEqual(vela.ponto_de_fechamento, vela.ponto_atual)

        vela.ponto_de_fechamento = 900
        self.assertEqual(vela.ponto_de_fechamento, vela.ponto_atual)
        self.assertEqual(900, vela.ponto_de_maxima)

        vela.ponto_de_fechamento = -1000
        self.assertEqual(vela.ponto_de_fechamento, vela.ponto_atual)
        self.assertEqual(-1000, vela.ponto_de_minima)
