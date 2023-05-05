# Aplikacja-do-polecania-muzyki

![GitHub forks](https://img.shields.io/badge/Version-1.0-red)

Interface in Polish lang

instalacja bibliotek:

pip install -r requirements.txt

Wymagane api keye znajdują się w pliku .env.example należy utworzyć plik .env i podać tam swoje klucze według wzoru

Opis:
Znajduje piosenkę o podobnym brzmieniu na podstawie takich danych jak tempo nastrój energia itd
polecenie_muzyki to główna aplikacja która uruchamia trzy mniejsze

Aplikacja pobranie_piosneki pobiera od użytkownika nazwę oraz autora piosenki a nastęnie pobiera ze spotify i zapisuje informacje o piosence do pliku wynik2.json

Aplikacja AI to prosta sieć neuronowa która pobiera parametry z wynik2.json, przetwarza dane i zapisuje do pliku wynik3.json dane piosenki która według niej jest podobna do pobranej

Aplikacja zwrócenie_piosenki pobiera dane z pliku wynik3.json, prosi użytkownika o wybranie gatunku piosenki z tych które znajdują się na liście, wysyła dane do spotify o wymaganiach utworu i następnie sciąga nam odpowiednią piosenkę

Podany gatunek nie musi się równać gatunkowi piosenki którą podaliśmy wcześniej! Jeśli podamy inny gatunek to dostaniemy piosenkę brzmiącą podobnie do orginału w tym gatunku który podaliśmy na koniec.

Testy zawiera test który sprawdza czy gatunki na liscie gatunki.txt rzeczywiście istnieją na spotify. Jeśli brakuje tam twojego ulubionego można go dopisać a następnie uruchomić test.

