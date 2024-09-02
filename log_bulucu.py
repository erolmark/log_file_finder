from urllib.request import Request, urlopen, URLError, HTTPError

def Space(j):
    i = 0
    while i <= j:
        print(" ", end='')
        i += 1
    print()  # Satır sonu

def findAdmin():
    with open("link.txt", "r") as f:
        link = input("Site İsmini Gir \n(örnek : example.com or www.example.com ): ")
        print("\n\n Mevcut Linkler: \n")
        while True:
            sub_link = f.readline().strip()
            if not sub_link:
                break
            req_link = f"http://{link}/{sub_link}"
            req = Request(req_link)
            try:
                response = urlopen(req)
            except HTTPError as e:
                continue
            except URLError as e:
                continue
            else:
                print("Başarılı Log Dosyası=> ", req_link)

def Credit():
    Space(9); print("#####################################")
    Space(9); print("#   +++ Log Dosyası Bulucu +++   #")
    Space(9); print("#     Developers Veraildez&Medusa   #")
    Space(9); print("#    Versa Community Versa Team   #")
    Space(9); print("#####################################")
    print("Daha yapım aşamasındadır. Siteyi yazarken sonuna / koymayın!")

Credit()
findAdmin()
