import yt_dlp


def format_url(url: str):
    index = url.find("&list")
    if index != -1:
        url = url[:index]
    return url


def get_video_infor(url: str):
    """
    Retrieves metadata information for a video without downloading it.

    :param url: The URL of the video to extract information from.
    :return: A dictionary containing video metadata if successful, otherwise None.
    """
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info
    except Exception as e:
        print(f"Lỗi: {e}")
        return None


def available_resolution(url: str):
    """
    Prints available MP4 video formats (format ID, resolution, and size) for a given video URL.

    :param url: The URL of the video to inspect.
    """
    video_info = get_video_infor(url)

    print(f"Tiêu đề: {video_info.get('title')}")
    print(f"Thumbnail: {video_info.get('thumbnail')}")
    print(f"Thời lượng: {video_info.get('duration_string')}")

    print("\n--- Các định dạng Video (MP4) ---")
    print(f"{'ID':<8} | {'Resolution':<12} | {'Size':>7}")
    for f in video_info.get('formats', []):
        if f.get('vcodec') != 'none' and f.get('ext') == 'mp4':
            filesize_mb = f.get('filesize') or f.get('filesize_approx')
            if filesize_mb:
                filesize_mb = round(filesize_mb / 1024 / 1024, 2)
                print(f"{f.get('format_id'):<8} | {f.get('resolution', 'audio-only'):<12} | {filesize_mb:>7} MB")


def download_specific_format(url: str, format_id: int, output_path="./downloads/%(title)s.%(ext)s"):
    """
    Downloads a video using a specific format ID.

    :param url: The URL of the video to download.
    :param format_id: The format ID to use for downloading.
    :param output_path: Output path template for saving the video.
    """
    format_string = f"{format_id}+bestaudio"
    ydl_opts = {
        'format': format_string,
        'outtmpl': output_path,
        'merge_output_format': 'mp4',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print('Tải video thành công.')
    except Exception as e:
        print(f"Lỗi tải xuống: {e}")


def download_mp3(url: str, output_path="./downloads/%(title)s.%(ext)s"):
    """
    Downloads the audio from a video and converts it to MP3 format.

    :param url: The URL of the video to extract audio from.
    :param output_path: Output path template for saving the MP3 file.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }
        ],
        'outtmpl': output_path,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Tải và chuyển đổi MP3 thành công")
    except Exception as e:
        print(f"Lỗi tải xuống MP3: {e}")