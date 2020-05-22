"""
Writes a CSV file using a list and DictWriter.

We then define the fields we’re going to be using into a variable called
fields. We then instantiate our CSV writer object and pass two arguments. The
first is output_csv, the file handler object. The second is our list of fields
fields which we pass to the keyword parameter fieldnames.

Now that we’ve instantiated our CSV file writer, we can start adding lines
to the file itself! First we want the headers, so we call .writeheader() on
the writer object. This writes all the fields passed to fieldnames as the
first row in our file. Then we iterate through our big_list of data.

Each item in big_list is a dictionary with each field in fields as the keys.
We call output_writer.writerow() with the item dictionaries which writes each
line to the CSV file.
"""

# Example:
import csv

big_list = [{'name': 'Fredrick Stein', 'userid': 712359021, 'is_admin': False},
            {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False},
            {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False},
            {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}]

with open('output.csv', 'w') as output_csv:
    fields = ['name', 'userid', 'is_admin']
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)

    output_writer.writeheader()
    for item in big_list:
        output_writer.writerow(item)


access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'},
              {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'},
              {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'},
              {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'},
              {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'},
              {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'},
              {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'},
              {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'},
              {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'},
              {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]

fields2 = ['time', 'address', 'limit']


with open('logger.csv', 'w') as logger_csv:
    log_writer = csv.DictWriter(logger_csv, fieldnames=fields2)

    log_writer.writeheader()
    for log in access_log:
        log_writer.writerow(log)
