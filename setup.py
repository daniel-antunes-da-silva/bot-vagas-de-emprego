import sys
import os
from cx_Freeze import setup, Executable

# Definir o q deve ser incluído na pasta final
arquivos = ['funcoes.py']

# Saída de arquivos
configuracao = Executable(
    script='monitoramento_vagas.py',
    icon='curriculo.ico'
)
# Configurar o executável
setup(
    name='Bot Indeed',
    version='1.0',
    description='Este programa varre vagas de emprego no site indeed.',
    author='Daniel Antunes',
    options={'build_exe': {
        'include_files': arquivos,
        'include_msvcr': True  # importante para rodar no WINDOWS.
    }},
    executables=[configuracao]
)
