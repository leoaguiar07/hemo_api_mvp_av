# **** SANGUE ****

# TIPOS SANGUÍNEOS
TIPO_SANGUE_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ('O', 'O'),
)

# FATOR RH
FATOR_RH_CHOICES = (
    ('+', '+'),
    ('-', '-'),
)

# ORIGEM DE RECEBIMENTO DO SANGUE (COLETA = DOAÇÃO/MOVIMENTAÇÃO = RECEBIDO POR OUTRO HEMOCENTRO)
ORIGEM_TIPO_CHOICES = (
    ('coleta', 'Coleta'),
    ( 'movimentacao','Movimentação')
)

# STATUS DO SANGUE COLETADO
STATUS_SANGUE_CHOICES = (
    ('disponivel', 'Disponível'),
    ('recebido','Disponível/Recebido'),
    ('enviado', 'Indisponível/Enviado'),
    ('vencido', 'Indiponível/Vencido')
)


# **** CADASTROS ****

# GÊNEROS
GENEROS_CHOICES = (
    ('Homem cisgênero', 'Homem Cisgênero'),
    ('Mulher cisgênero', 'MULHER cisgênero'),
    ('HOMEM transgênero', 'HOMEM transgênero'),
    ('Mulher transgênero', 'Mulher transgênero'),
    ('Não-binário', 'Não-binário'),
    ('Agênero', 'Agênero'),
)
