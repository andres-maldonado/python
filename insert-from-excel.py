### GET OR CREATE MANUAL
goc_my_obj('TABLE_NAME', **{'Id': 1, 'Name': 'asd'})

goc_my_obj(table, **kwargs):
    query = ''
    for key, value in kwargs.items():
        query += '{}={};'.format(key, value)
    
    main_query = 'SELECT * FROM {table} WHERE {query}'.format(table=table, query=query)
    
    try:
        executor(main_query)
    except:
        create_in_db(table, query)


import csv
import io

csv_file = request.FILES['file']
data_set = csv_file.read().decode('UTF-8')
io_string = io.StringIO(data_set)
new_clients = 0

for column in csv.reader(io_string):
    created_time = column.index('created_time')
    email = column.index('email1')
    name = column.index('first_name')
    lastname = column.index('last_name')
    phone = column.index('phone_work')
    ciudad = column.index('city')
    break

for column in csv.reader(io_string):
    date_block = (column[created_time]).split('T')
    days = date_block[0].split('-')
    hours = date_block[1].split('-')
    hours = hours[0].split(':')
    current_date = datetime(int(days[0]), int(days[1]), int(days[2]), int(hours[0]), int(hours[1]), int(hours[2]))
    main_phone = (column[phone]).replace('+', '')

    if main_phone[2] is '0':
        new_phone = list(main_phone)
        new_phone[2] = ''
        current_phone = ''.join(new_phone)
    else:
        current_phone = main_phone

    try:
        obj, created = Prospect.objects.get_or_create(
            first_name=column[name],
            last_name=column[lastname],
            email=column[email],
            whatsapp=current_phone,
            phone=current_phone,
            city=column[ciudad],
            created_in_facebook=current_date,
        )
        new_clients = new_clients + 1
    except Exception:
        messages.error(request, 'Error fatal con %s %s %s %s %s' % (str(column[name]), str(column[lastname]), str(current_phone), str(column[ciudad]), str(current_date)))
messages.success(request, '%d nuevos clientes potenciales han sido cargados con éxito' % new_clients)
