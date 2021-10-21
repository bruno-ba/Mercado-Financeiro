class Candlestick:
    tipo_vela_de_alta = 'alta'
    tipo_vela_de_baixa = 'baixa'
    tipo_vela_neutra = 'neutro'

    status_vela_em_formacao = 'em formação'
    status_vela_finalizado = 'finalizado'

    def __init__(self, ponto_de_abertura):
        self._ponto_de_fechamento = None
        self._ponto_de_abertura = ponto_de_abertura
        self._ponto_atual = self._ponto_de_minima = self._ponto_de_maxima = self._ponto_de_abertura

    @property
    def status_da_vela(self):
        return Candlestick.status_vela_em_formacao if self._ponto_de_fechamento is None else Candlestick.status_vela_finalizado

    @property
    def tipo_de_vela(self):
        if self._ponto_atual > self._ponto_de_abertura:
            return Candlestick.tipo_vela_de_alta
        elif self.ponto_atual < self._ponto_de_abertura:
            return Candlestick.tipo_vela_de_baixa
        else:
            return Candlestick.tipo_vela_neutra

    @property
    def ponto_de_abertura(self):
        return self._ponto_de_abertura

    @ponto_de_abertura.setter
    def ponto_de_abertura(self, new_value):
        self._ponto_de_abertura = new_value

    @property
    def ponto_de_fechamento(self):
        return self._ponto_de_fechamento

    @ponto_de_fechamento.setter
    def ponto_de_fechamento(self, new_value):
        self._ponto_de_fechamento = new_value
        if self.status_da_vela is Candlestick.status_vela_finalizado:
            self._ponto_atual = self._ponto_de_fechamento
            self._ponto_de_minima = min(self._ponto_de_minima, self._ponto_atual)
            self._ponto_de_maxima = max(self._ponto_de_maxima, self._ponto_atual)

    @property
    def ponto_de_minima(self):
        return self._ponto_de_minima

    @ponto_de_minima.setter
    def ponto_de_minima(self, new_value):
        self._ponto_de_minima = min(self._ponto_de_minima, new_value)
        self._ponto_de_maxima = max(self._ponto_de_minima, self._ponto_de_maxima)

    @property
    def ponto_de_maxima(self):
        return self._ponto_de_maxima

    @ponto_de_maxima.setter
    def ponto_de_maxima(self, new_value):
        self._ponto_de_maxima = max(self._ponto_de_maxima, new_value)
        self.ponto_de_minima = min(self._ponto_de_minima, self._ponto_de_maxima)

    @property
    def ponto_atual(self):
        return self._ponto_atual

    @ponto_atual.setter
    def ponto_atual(self, new_value):
        if self.status_da_vela is Candlestick.status_vela_em_formacao:
            self._ponto_atual = new_value
            self._ponto_de_minima = min(self._ponto_de_minima, self._ponto_atual)
            self._ponto_de_maxima = max(self._ponto_de_maxima, self._ponto_atual)
