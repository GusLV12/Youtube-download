import pytube

try:
    video_url = input("Ingresa url a descargar: ")
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.get_highest_resolution()
    video.download(r'C:/Users/LINKZ/OneDrive/Escritorio')
    print("Descarga completada.")
except pytube.exceptions.PytubeError as e:
    print("Ha ocurrido un error:", e)