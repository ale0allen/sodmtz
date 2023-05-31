class Vinculo:
    def __init__(self, cpf_usuario=None, id_perfil=None):
        if cpf_usuario is None:
            self.id_usuario = ''
        else:
            self.id_usuario = cpf_usuario
        if id_perfil is None:
            self.id_perfil = ''
        else:
            self.id_perfil = id_perfil
