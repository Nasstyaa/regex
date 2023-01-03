from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phone_book.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Создаем новый список контактов, где ФИО помещены в отдельные столбцы lastname, firstname, surname

new_list = []
for contact in contacts_list:
    contact[:3] = [' '.join(contact[:3])]
    new_list.append(contact)

new_contact_list = []
for el in new_list:
    for record in el:
        record = el[0].split()
        record.extend(el[1:])
    new_contact_list.append(record)

# Приводим все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;

pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)' \
          '(\s*)(\-*)(\d{3})(\-)*(\d{2})(\-)*(\d{2})*' \
          '(\s)*(\()*(доб\.)*(\s)*(\d+)*(\))*'

repl = r'+7(\4)\8-\10-\12 \15\17'

new_list = []
for new_contact in new_contact_list:
    contacts_string = ','.join(new_contact)
    new_contacts_string = re.sub(pattern, repl, contacts_string)
    format_contacts = new_contacts_string.split(',')
    new_list.append(format_contacts)
pprint(new_list)