import csv

spisok = []
with open('travel_notes.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    spisok.append(row)

l = input()
want_to_be = []
already_be = []

for name in spisok:
  if l == name[0][0]:
    already_be.append(name[1].split(';'))
    want_to_be.append(name[2].split(';'))

already_be_sort = list(
    set([gorod for podspisok in already_be for gorod in podspisok]))
want_to_be_sort = list(
    set([gorod for podspisok in want_to_be for gorod in podspisok]))

unic_city_to_be = []
for city in want_to_be_sort:
  if city not in already_be_sort:
    unic_city_to_be.append(city)

already_be_sort = sorted(already_be_sort)
want_to_be_sort = sorted(want_to_be_sort)
unic_city_to_be = sorted(unic_city_to_be)

v_ioge_edem = ''
for city in unic_city_to_be:
  if city in want_to_be_sort:
    v_ioge_edem = city
    break

already_be_sort_itog = f"Успели побывать: {', '.join(already_be_sort)} \n"
want_to_be_sort_itog = f"Хотим побывать: {', '.join(want_to_be_sort)} \n"
unic_city_to_be_itog = f"Никто не был в: {', '.join(unic_city_to_be)} \n"
v_ioge_edem_itog = f"В итоге едем в: {v_ioge_edem}"

lines = [
    already_be_sort_itog, want_to_be_sort_itog, unic_city_to_be_itog,
    v_ioge_edem_itog
]

with open('vacation.csv', 'w', encoding='utf-8') as file:
  file.writelines(lines)
