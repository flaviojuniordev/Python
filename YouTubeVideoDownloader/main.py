from yt_dlp import YoutubeDL

# URL do vídeo
url = 'cole sua url aqui'

# Configurações de download
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',  # Salva o vídeo com o título original
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)  # Baixa o vídeo
    print("Título do vídeo:", info.get('title'))
    print("Download concluído!")
