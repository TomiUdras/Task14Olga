def read_csv(filename):
  """
  Reads a CSV file and returns a list of lists, where each inner list represents a row.
  """
  data = []
  with open(filename, 'r') as file:
    for line in file:
      row = [cell.strip('"') for cell in line.strip().split(',')]
      data.append(row)
  return data


spisok = read_csv('travel_notes.csv')

l = input()
want_to_be = []
already_be = []

for row in spisok:
  if l == row[0][0]:
    already_be.append(row[1].split(';'))
    want_to_be.append(row[2].split(';'))

already_be_sort = list(
    set([gorod for sublist in already_be for gorod in sublist]))
already_be_sort.sort()

want_to_be_sort = list(
    set([gorod for sublist in want_to_be for gorod in sublist]))
want_to_be_sort.sort()

unic_city_to_be = [
    city for city in want_to_be_sort if city not in already_be_sort
]

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

