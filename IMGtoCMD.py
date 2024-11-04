from PIL import Image

def przetworz_obraz(nazwa_pliku, szerokosc_terminala=80, wysokosc_terminala=50):
    img = Image.open(nazwa_pliku)
    img = img.resize((szerokosc_terminala, wysokosc_terminala))
    img = img.convert("L")  # Konwertuje na obraz w odcieniach szarości

    dane_obrazu = list(img.getdata())
    szerokosc_obrazu = img.width

    # Zakresy kolorów dla każdego symbolu
    zakresy_kolorow = [0, 25.5, 51, 76.5, 102, 127.5, 153, 178.5, 204, 229.5, 255]

    # Mapa symboli ASCII
    mapa_znakow = [
        " ", ".", ":", "-", "=", "+", "*", "#", "%", "@", "█"
    ]

    obraz_wynikowy = ""

    for i in range(0, len(dane_obrazu), szerokosc_terminala):
        wiersz = dane_obrazu[i:i + szerokosc_terminala]
        for piksel in wiersz:
            for indeks, zakres in enumerate(zakresy_kolorow[:-1]):
                if zakres <= piksel <= zakresy_kolorow[indeks + 1]:
                    symbol = mapa_znakow[indeks]
                    obraz_wynikowy += symbol
                    break
            else:
                obraz_wynikowy += " "
        obraz_wynikowy += "\n"

    return obraz_wynikowy

if __name__ == '__main__':
    nazwa_pliku = 'img/obraz.jpg'
    wynik_ascii = przetworz_obraz(nazwa_pliku)
    print(wynik_ascii)
