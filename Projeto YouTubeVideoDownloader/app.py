from yt_dlp import YoutubeDL
from tkinter import messagebox
import threading
from interface import create_interface

ydl_opts = {
    "format": "bestvideo[height<=1080]+bestaudio/best", 
    "outtmpl": "%(title)s.%(ext)s", 
    "merge_output_format": "mp4", 
}

def download_video(url, update_progress, reset_ui):

    try:

        def progress_hook(d):
            if d["status"] == "downloading":
                total_bytes = d.get("total_bytes", 0) or d.get(
                    "total_bytes_estimate", 0
                )
                downloaded_bytes = d.get("downloaded_bytes", 0)

                if total_bytes > 0:
                    percent = (downloaded_bytes / total_bytes) * 100
                    update_progress(percent, f"{percent:.2f}%")
            elif d["status"] == "finished":
                update_progress(100, "100%")

        # Adiciona o hook de progresso dinamicamente às opções
        ydl_opts["progress_hooks"] = [progress_hook]

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            messagebox.showinfo(
                "Sucesso", f"Download concluído!\nTítulo: {info.get('title')}"
            )
    except Exception as ex:
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o vídeo: {ex}")
    finally:
        reset_ui()


def start_download(url, update_progress, reset_ui):

    threading.Thread(
        target=download_video, args=(url, update_progress, reset_ui)
    ).start()


if __name__ == "__main__":
    create_interface(start_download)
