# timesheet2invoice
Convert a csv based timesheet to an weekly invoice

## Install
Clone this repository and:
```
$ pip install requirements.txt
```

## Usage
Given the following example timesheet saved as `test.csv`:
```
160115, 8, Task A
160116, 8.5, Another task
________________

160127, 7, Did something
```

To convert this into a weekly invoice:
```
$ python timesheet2invoice.py test.csv
Week    Hours   Notes
2       16.5    Task A; Another task
4       7.0     Did something
```

It will skip all the invalid rows. It will concatenate all other columns that are not the date and time into a ; seperated line. The following options are available (from `--help`):
```
$ python timesheet2invoice.py --help
Usage: timesheet2invoice.py [OPTIONS] CSV_FILE

Options:
  --columns <columns>  Sets target columns  [default: Date,Hours,Notes]
  --dateColumn TEXT    Name of date column (must match header)  [default:
                       Date]
  --hoursColumn TEXT   Name of hours column (must match header)  [default:
                       Hours]
  --dateFormat TEXT    Date format  [default: %y%m%d]
  --help               Show this message and exit.
```