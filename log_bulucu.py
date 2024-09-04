from urllib.request import Request, urlopen, URLError, HTTPError

def print_spaces(count):
    """Satır başında verilen sayıda boşluk karakteri basar."""
    print(" " * count, end='')

def find_admin():
    """Linkler dosyasındaki her bir bağlantıyı kontrol eder ve başarılı olanları basar."""
    with open("link.txt", "r") as f:
        link = input("Site İsmini Gir \n(örnek : example.com veya www.example.com ): ")
        print("\n\nMevcut Linkler:\n")
        while True:
            sub_link = f.readline().strip()
            if not sub_link:
                break
            req_link = f"http://{link}/{sub_link}"
            req = Request(req_link)
            try:
                response = urlopen(req)
            except HTTPError:
                continue
            except URLError:
                continue
            else:
                print("Başarılı Log Dosyası=>", req_link)

def print_banner():
    """Programın başlık ve bilgi kısmını basar."""
    print_spaces(9)
    print("#####################################")
    print_spaces(9)
    print("#   +++ Log Dosyası Bulucu +++   #")
    print_spaces(9)
    print("#     Developers Veraildez&Medusa   #")
    print_spaces(9)
    print("#    Versa Community Versa Team   #")
    print_spaces(9)
    print("#####################################")

def main():
    """Ana fonksiyon: banner ve find_admin işlevlerini çağırır."""
    print_banner()
    find_admin()

if __name__ == "__main__":
    main()
