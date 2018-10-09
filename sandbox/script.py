import csv
import json

data = {}

with open('input2.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        year = row['year']

        if not year in data:
            data[year] = []

        node = {
            'i': row['target'],
            'wc': 'mil',
            'e': row['source'],
            'v': int(float(row['fob']))
        }

        data[year].append(node)

    output = {
        'timeBins': []
    }

    for key in data:
        output['timeBins'].append({
            'data': data[key],
            't': int(key)
        })

    with open('wood-data.json', 'w') as outfile:
        json.dump(output, outfile)
