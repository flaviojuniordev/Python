# YouTube Video Downloader

Este é um projeto simples para baixar vídeos do YouTube utilizando a biblioteca `yt_dlp`, uma ferramenta poderosa que facilita o download de vídeos na melhor qualidade disponível. Este projeto baixa o vídeo e o salva com o título original do vídeo.

## Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.6 ou superior é recomendada).

## Dependências

Este projeto requer a instalação da biblioteca `yt_dlp`. Siga as instruções abaixo para instalá-la:

```bash
pip install yt-dlp
```

## Uso

1. Clone este repositório ou copie o código para um arquivo `.py`.
2. Execute o script.

O script está configurado para baixar o vídeo na URL especificada e salvá-lo no diretório onde o script está localizado.

## Código

Abaixo está o código principal do projeto:

```python
from yt_dlp import YoutubeDL

# URL do vídeo
url = 'https://www.youtube.com/watch?v=pqSUPCK1pqw'

# Configurações de download
ydl_opts = {
    'format': 'best',  # Altera a qualidade do vídeo
    'outtmpl': '%(title)s.%(ext)s',  # Salva o vídeo com o título original
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)  # Baixa o vídeo
    print("Título do vídeo:", info.get('title'))
    print("Download concluído!")
```

## Executando o Código

Para rodar o código, basta executar o seguinte comando no terminal:

```bash
python nome_do_arquivo.py
```

O vídeo será baixado com o título original do YouTube e salvo no mesmo diretório (ou no diretório especificado).

## Observação

Para baixar vídeos de URLs diferentes, altere o valor da variável `url` no código. 

## Licença

Este projeto é de código aberto e está licenciado sob a MIT License. Sinta-se livre para usá-lo e modificá-lo conforme necessário.
