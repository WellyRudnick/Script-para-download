import yt_dlp as dlp

def Download():
    # URLs dos vídeos para download
    urls = [
        "",  # Insira a URL do vídeo aqui
        # "", # Insira a URL do vídeo aqui
        # "", # Insira a URL do vídeo aqui
        # "", # Insira a URL do vídeo aqui
    ]

    # Pergunta ao usuário o tipo de download desejado
    download_choice = input("Digite 'mp3' para baixar apenas o áudio em MP3 ou 'mp4' para baixar o vídeo em MP4: ").strip().lower()
    # Configurações do downloader
    if download_choice == 'mp3':
        options = {
            'format': 'bestaudio/best',           # Baixa o melhor formato de áudio disponível
            'concurrent_fragments': 500,          # Número de fragmentos simultâneos ****IMPORTANTE**** ALTERAR CONFORME SUA CONEXÃO DE INTERNET ****IMPORTANTE****
            'retries': 'infinite',                # Tentativas ilimitadas em caso de falha
            'fragment_retries': 5,                # Tentativas de rebaixar fragmentos com erro
            'external_downloader': 'aria2c',      # Usa aria2c como downloader externo
            'external_downloader_args': ['-x16'], # Até 16 conexões por arquivo no aria2c
            'postprocessors': [{                  # Pós-processador para converter em MP3
                'key': 'FFmpegExtractAudio',      # Utiliza o FFmpeg para extrair o áudio
                'preferredcodec': 'mp3',          # Define o codec do áudio para MP3
                'preferredquality': '320',        # Define a qualidade para 320 kbps
            }],
            
            'outtmpl': r'Downloads/%(title)s.%(ext)s',  # Caminho e nome do arquivo
        }
    elif download_choice == 'mp4':
        options = {
            'format': 'bestvideo+bestaudio/best',  # Baixa o melhor vídeo + áudio combinados            
            'concurrent_fragments': 500,           # Número de fragmentos simultâneos ****IMPORTANTE**** ALTERAR CONFORME SUA CONEXÃO DE INTERNET ****IMPORTANTE****
            'retries': 'infinite',                 # Tentativas ilimitadas em caso de falha
            'fragment_retries': 5,                 # Tentativas de rebaixar fragmentos com erro
            'external_downloader': 'aria2c',       # Usa aria2c como downloader externo            
            'external_downloader_args': ['-x16'],  # Até 16 conexões por arquivo no aria2c            
            'outtmpl': r'Downloads/%(title)s.%(ext)s',  # Caminho e nome do arquivo
        }
    else:
        print("Escolha inválida. Execute o programa novamente e digite 'mp3' ou 'mp4'.")
        exit()

    # Inicializa e realiza o download
    with dlp.YoutubeDL(options) as ydl:
        for url in urls:
            ydl.download([url])


# Inicializa o download
Download()
