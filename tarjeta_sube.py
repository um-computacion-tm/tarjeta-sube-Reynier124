class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass
PRECIO_TICKET = 70
PRIMARIO = 'primario'
ACTIVADO = 'activado'
DESACTIVADO = 'desactivado'
SECUNDARIO = 'secundario'
UNIVERSITARIO = 'universitario'
JUBILADO = 'jubilidado'
DESCUENTOS = {
    PRIMARIO: 0.50,
    SECUNDARIO: 0.60,
    UNIVERSITARIO: 0.70,
    JUBILADO: 0.75,
}
class Sube():
    def __init__(self, param_saldo = 0, param_grupo_beneficiario = None, param_estado = 'activado'):
        self.saldo = param_saldo
        self.grupo_beneficiario = param_grupo_beneficiario
        self.estado = param_estado
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == None:
            return PRECIO_TICKET
        else:
            for i, x in DESCUENTOS.items():
                    if self.grupo_beneficiario == i:
                        return PRECIO_TICKET * x
    def pagar_pasaje(self):
        if self.estado == ACTIVADO:
            if self.grupo_beneficiario == None and self.saldo >= PRECIO_TICKET:
                self.saldo -= PRECIO_TICKET
            elif self.grupo_beneficiario == None and self.saldo < PRECIO_TICKET:
                raise NoHaySaldoException('Saldo insuficiente')
            else: 
                for i, x in DESCUENTOS.items():
                    if self.grupo_beneficiario == i and self.saldo >= PRECIO_TICKET*x:
                        self.saldo -= PRECIO_TICKET*x
                    elif self.grupo_beneficiario == i and self.saldo >= PRECIO_TICKET*x:
                        NoHaySaldoException('Saldo insuficiente')
        elif self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException('Tarjeta desactivada')
        '''if self.grupo_beneficiario == None and self.saldo >= PRECIO_TICKET and self.estado == 'activado':
            self.saldo -= PRECIO_TICKET
        elif self.grupo_beneficiario == PRIMARIO and self.saldo >= PRECIO_TICKET/2 and self.estado == 'activado':
            self.saldo -= PRECIO_TICKET / 2
        elif self.grupo_beneficiario == None and self.saldo < PRECIO_TICKET and self.estado == 'activado':
            raise NoHaySaldoException('Insuficiente saldo')
        elif self.grupo_beneficiario == PRIMARIO and self.saldo > PRECIO_TICKET/2 == 'activado':
            self.saldo -= PRECIO_TICKET / 2
        else:
            raise UsuarioDesactivadoException('Tarjeta desactivada')'''
        
    def cambiar_estado(self, estado):
        if estado == 'pendiente':
            raise EstadoNoExistenteException()
        else:
            self.estado = estado