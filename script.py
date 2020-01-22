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

# html string to be executed
html_str = """



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" type="text/css" href="template.css">
    <title>CSV to Html</title>
</head>
<body>
    <div class="container">
        <h1>Welcome! Write your article here</h1>
        <div id="titlediv">
            <input id="title" type="text" placeholder="{h1}">
        </div>
        <div id="subtitlediv">
            <input id="subtitle" type="text" placeholder="{h2}">
        </div>
        <div id="articlediv">
            <textarea id="article" rows="5" cols="100" placeholder="{article}">
               
                </textarea>
        </div>
        <div>
            <input type="submit" value="Submit">
        </div>
    </div>
    
</body>
</html>
""".format(h1=csv_list[0],h2=csv_list[1],article=csv_list[2])

# generate the html file
try:
        with open('template.html','w') as htmlfile:
            htmlfile.write(html_str)
except Exception as err:
    print(err)