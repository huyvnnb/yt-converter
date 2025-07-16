import pyfiglet
import yt_dlp

from converter import format_url, available_resolution, download_specific_format, download_mp3


# ==== Các hàm đã có ====
# ... (giữ nguyên các hàm format_url, get_video_infor, available_resolution, download_specific_format, download_mp3) ...


def print_banner():
    banner = pyfiglet.figlet_format("YOUTUBE DOWNLOADER", font="slant")
    print(banner)


def print_menu():
    print("\n==== MENU ====")
    print("1. Xem các định dạng video")
    print("2. Tải video theo định dạng cụ thể")
    print("3. Tải MP3 từ video")
    print("0. Thoát")


def main():
    print_banner()
    while True:
        print_menu()
        choice = input("Chọn chức năng (0-3): ").strip()

        if choice == "1":
            url = input("Nhập URL video: ").strip()
            url = format_url(url)
            available_resolution(url)

        elif choice == "2":
            url = input("Nhập URL video: ").strip()
            url = format_url(url)
            format_id = input("Nhập format_id muốn tải: ").strip()
            if format_id.isdigit() or format_id.isalnum():
                download_specific_format(url, format_id)
            else:
                print("Format ID không hợp lệ.")

        elif choice == "3":
            url = input("Nhập URL video: ").strip()
            url = format_url(url)
            download_mp3(url)

        elif choice == "0":
            print("Thoát chương trình. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
