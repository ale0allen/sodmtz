class Perfil:
    def __init__(self, codigo_perfil=None, nome_perfil=None, nome_sistema=None,  descricao_perfil=None):
        if codigo_perfil is None:
            self.codigo_perfil =  ""
        else:
            self.codigo_perfil = codigo_perfil
        if nome_perfil is None:
            self.nome_perfil = ""
        else:
            self.nome_perfil = nome_perfil
        if nome_sistema is None:
            self.nome_sistema = ""
        else:
            self.nome_sistema = nome_sistema
        if descricao_perfil is None:
            self.descricao_perfil = ""
        else:
            self.descricao_perfil = descricao_perfil


