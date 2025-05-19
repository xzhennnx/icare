pip install yt-dlp

yt-dlp -x --audio-format mp3 -o "video_audio.%(ext)s" "https://www.youtube.com/watch?v=影片ID"

import yt_dlp

channel_url = "https://www.youtube.com/c/@icare愛健康"

def get_video_urls(channel_url):
 ydl_opts = {
 "quiet": True,
 "extract_flat": True, }

 with yt_dlp.YoutubeDL(ydl_opts) as ydl:
 info = ydl.extract_info(channel_url, download=False)

 if not info or "entries" not in info:
print("無法獲取影片列表，請檢查網址或嘗試使用 cookies.txt")
return []

video_urls = ["https://m.youtube.com/channel/UCsUSffSkOgPT43rKqRuydIg"]

return video_urls

video_urls = get_video_urls(channel_url)
print(f"找到 {len(video_urls)} 部影片！")
print(video_urls[:5])  # 只顯示前 5 部影片的網址