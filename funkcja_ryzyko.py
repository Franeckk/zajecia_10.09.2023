#  funkcja poziom_ryzyka zwraca liczbę od 0 do 10, która okresla poziom ryzyka,
#  gdzie 0 - brak ryzyka; 10 - ekstremalnie wysokie ryzyko
def poziom_ryzyka(wiek, plec, wyksztalcenie):
   if plec == "K":
       return 1
   else:
       return 0

   if wyksztalcenie == "Podstawowe":
       return 1
   else:
       return 0



