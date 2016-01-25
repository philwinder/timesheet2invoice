import click
import datetime
import collections
import csv

cols = ['Date', 'Hours', 'Notes']

@click.command()
@click.argument('csv_file', type=click.Path(exists=True))
@click.option('--columns', is_flag=False, default=','.join(cols), show_default=True, metavar='<columns>', type=click.STRING, help='Sets target columns')
@click.option('--dateColumn', default=cols[0], show_default=True, help='Name of date column (must match header)')
@click.option('--hoursColumn', default=cols[1], show_default=True, help='Name of hours column (must match header)')
@click.option('--dateFormat', default="%y%m%d", show_default=True, help='Date format')
def main(csv_file, columns, datecolumn, hourscolumn, dateformat):
    # split columns by ',' and remove whitespace
    columns = [c.strip() for c in columns.split(',')]

    output = []
    with open(csv_file, mode='r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if len(row) != len(columns):
                continue
            dict = {}
            for x, val in enumerate(columns):
                dict[val] = row[x].strip()
            output.append(dict)

    # click.echo(json.dumps(output, indent=2, sort_keys=True))

    weekList = {}

    for day in output:
        d = datetime.datetime.strptime( day[datecolumn], dateformat)
        week = d.isocalendar()[1]
        hours = float(day[hourscolumn])
        everythingElse = day.copy()
        everythingElse.pop('Date')
        everythingElse.pop('Hours')
        value = '; '.join([value for key, value in everythingElse.items()])
        if weekList.has_key(week):
            weekList[week] = [weekList[week][0] + hours, weekList[week][1] + '; ' + value]
        else:
            weekList[week] = [hours, value]

    od = collections.OrderedDict(sorted(weekList.items()))

    click.echo("%s\t%s\t%s" % ('Week', hourscolumn, 'Notes'))
    for week in od:
        click.echo("%s\t%s\t%s" % (week, od[week][0], od[week][1]))

main()
