# inheritance- rozszerzenie programu do zarządzania plikami csv

W przypadku formatu pickle, json, pliki zapisywane są jako listy list - każdy rząd to lista ciągów znaków, rzędy są przechowywane w liście.

Napisz program "reader.py", który zmodyfikuje plik csv, json, lub pickle <src> i wyświetli w terminalu jego zawartość, a następnie zapisze w wybranej lokalizacji.
Wykonanie programu:

reader.py <src> <dst> <change1> <change2> ..
src to ścieżka pliku csv. Jeśli plik nie istnieje bądź podana ścieżka nie jest plikiem, wyświetl błąd i wskaż pliki w tym samym katalogu.
dst to docelowa ścieżka w której zapiszemy zmieniony plik csv.

change1 ... changeN to ciągi znaków w postaci "Y,X,wartosc" Y. to wiersz do zmodyfikowania (liczony od 0), X to kolumna (liczona od 0). Komórka pod wskazanym adresem powinna zmienić wartość na "wartosc".

Rodzaj pliku (src i dst) powinien być wykrywany na podstawie rozszerzenia:
*.csv - plik csv
*.json - plik json
*.pickle - plik pickle
