
# YouTube Video Downloader com Interface

Este é um projeto aprimorado para baixar vídeos do YouTube, agora com uma interface gráfica intuitiva, que permite aos usuários colar o link do vídeo e gerenciar o download facilmente. O projeto utiliza a biblioteca `yt_dlp` para gerenciar os downloads na melhor qualidade disponível.

## Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.6 ou superior é recomendada).

## Dependências

Este projeto requer a instalação das seguintes dependências:

- **yt_dlp**: Para gerenciar o download de vídeos.

### youtube-dl

[youtube-dl GitHub Repository](https://github.com/ytdl-org/youtube-dl)

**Descrição**: youtube-dl é uma ferramenta de linha de comando que permite baixar vídeos de YouTube e muitos outros sites de vídeo. É altamente configurável e suporta uma ampla variedade de formatos e opções de download.

**Principais recursos**:
- Suporte para download de vídeos de diversos sites.
- Opções para selecionar formato e qualidade dos vídeos.
- Integração com scripts e automações.

Instale a biblioteca `yt_dlp` com o seguinte comando:

```bash
pip3 install yt-dlp
```

- **FFmpeg**: Necessário para combinar áudio e vídeo em alta qualidade.

### FFmpeg

**Descrição**: O `ffmpeg` é essencial para manipulação de arquivos de áudio e vídeo e permite que o `yt_dlp` combine vídeo e áudio quando estes são disponibilizados separadamente em resoluções maiores.

**Instalação do FFmpeg**:
- **macOS**: `brew install ffmpeg`
- **Ubuntu/Debian**: `sudo apt update && sudo apt install ffmpeg`
- **Windows**: Baixe do [site oficial do FFmpeg](https://ffmpeg.org/download.html) e configure o caminho na variável de ambiente **PATH**.

## Interface Gráfica

A interface gráfica permite que o usuário insira o link do vídeo, visualize e inicie o download com um clique. Para usar, basta iniciar o programa e colar o link do YouTube no campo designado.

<img src="imgs/interfacevideodownload-1.jpg">
<img src="imgs/interfacevideodownload-2.jpg">

### Capturas de Tela

Aqui você pode adicionar capturas de tela da interface para ilustrar como utilizá-la:

- **Tela Inicial**: Campo para inserir o link do vídeo e botão de download.
- **Tela de Progresso**: Exibe o progresso do download.

> **Nota**: Cole os prints da interface aqui.

## Uso

1. Clone este repositório ou copie o código para um arquivo `.py`.
2. Execute o script.
   
O script está configurado para baixar o vídeo na URL especificada e salvá-lo no diretório onde o script está localizado.

## Código

Aqui está um trecho do código principal:

```python
from yt_dlp import YoutubeDL
import tkinter as tk

# Configurações de download
ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'merge_output_format': 'mp4',
}

# Interface gráfica para colar o link e iniciar o download
def baixar_video():
    url = entrada.get()
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print("Título do vídeo:", info.get('title'))
        print("Download concluído!")

# Configuração da interface
app = tk.Tk()
app.title("YouTube Downloader")
app.geometry("400x200")

label = tk.Label(app, text="Cole o link do vídeo:")
label.pack()

entrada = tk.Entry(app, width=50)
entrada.pack()

botao = tk.Button(app, text="Baixar", command=baixar_video)
botao.pack()

app.mainloop()
```

## Ambiente virtual

Recomenda-se o uso de um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate  # Windows
```

Após ativar o ambiente virtual, instale a dependência `yt_dlp` conforme descrito acima.

## Observação

Para baixar vídeos de URLs diferentes, altere o valor da entrada de URL na interface.

## Licença

Este projeto é de código aberto e está licenciado sob a MIT License.
