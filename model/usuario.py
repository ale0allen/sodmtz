class Usuario:
    def __ini__(self, cpf_usuario=None, nome_usuario=None):
        if cpf_usuario is None:
            self.cpf_usuario = ""
        else:
            self.cpf_usuario = cpf_usuario
        if nome_usuario is None:
            self.nome_usuario = ""
        else:
            self.nome_usuario = nome_usuario

