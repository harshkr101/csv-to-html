import csv
import itertools

csv_list = []

# read the csv file and append it to csv_list      
try:
    with open('template.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            csv_list.append(row)
except Exception as exception:
    print(exception)

# flatten the csv_list for simplified indexing
csv_list=list(itertools.chain(*csv_list))
html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>CSV to Html</title>
</head>
<body>
    <h1>{h1}</h1>
    <h2>{h2}</h2>
    <div class="container">
        <h3>
            {article}
        </h3>
    </div>
</body>
</html>
""".format(h1=csv_list[0],h2=csv_list[1],article=csv_list[2])

try:
        with open('template.html','w') as htmlfile:
            htmlfile.write(html_str)
except Exception as err:
    print(err)