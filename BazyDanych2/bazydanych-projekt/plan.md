# tworzenie schematu korzystajac z modelu pojeciowego bazy Ewidencji Gruntow i Budynkow (EGiB)

0. klasy z grupy DzialkaKlasoUzytek (+ referencje / dziedziczenie)
1. utworzyc tabele **delta_konturklasyfikacyjny(id serial PK, czaszmiany timestamp,delta liczba)**
2. integralnosc danych
3. efektywny dostep do danych (ograniczenia, indeksy)
4. atrybuty przestrzenne o wlasciwych typach, indeksy przestrzenne

# automatyzacja procesow

5. Po wykryciu próby aktualizacji geometrii w tabeli **egb_konturklasyfikacyjny** wprowadzą nowy rekord do tabeli **delta_konturklasyfikacyjny**. Rekord ma zawierać datę zmiany, i wartość różnicy powierzchni między aktualną, a poprzednią powierzchnią geometrii aktualizowanego obiektu.

# przetwarzanie danych (utworzyc funkcje ktora)

6. Utworzy tabelę **dzialki_klasa(id (serial) PK, geom(geometria), klasa(text), powierzchnia(liczba))**
7. Znajdzie wszystkie działki, które są wewnątrz obrębu, którego identyfikator został przekazany jako parametr funkcji.
8. Wyszuka wszystkie kontury klasyfikacyjne, które przecinają obręb i które mają wartość OZK przekazaną jako parametr funkcji
9. dla kazdej dzialki z pkt 7:
    a) przetnie jej geometrie z konturami z punktu 8
    b) obiekty powstale w efekcie przeciecia wprowadzi do tabeli **dzialki_klasa**
