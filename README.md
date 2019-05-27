# Zadanie rekrutacyjne ProfilSoftware

Zadanie rekrutacyjne na backend.

## Instalacja

Należy użyć [pip](https://pip.pypa.io/en/stable/) aby zainstalować zależności.

```bash
pip install -r requirements.txt
```

## Dostępne argumenty
**-h** - Pomoc wypisująca możliwe argumenty.

**average** - Średnia liczba osób która przystąpiła do egzaminu dla daneg województwa na przestrzeni lat, do podanego roku włącznie.

**percentage** - Procentowa zdawalność dla danego województwa na przestrzeni lat.

**best** - Województwo o najlepszej zdawalnośći w konkretnym roku.

**regression** - Wykrycie województw, które zanotowały regresję.

**comparison** - Porównanie dwóch województw.

**-filter** - Zastosowaniu filtru (dostępne filtry to: men, women, both)

## Przykład użycia

```bash
python main.py average -filter women
```

## Użyte biblioteki
Do pobierania danych z api użyta została biblioteka *requests* oraz *json*.

Do obsługi bazy danych została użyta biblioteka *sqlalchemy*.

Do testów została użyta biblioteka *pytest* oraz *pytest-mock*

## Biblioteki które mogły zostać użyte
Biblioteka *csv* albo *pandas* do przetwarzania plików csv.