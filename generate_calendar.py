import sys
from datetime import timedelta, date


def generate_calendar(year):
    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)


    def date_to_cell(date):
        weekend_class = ''
        if date.weekday() > 4:
            weekend_class = ' weekend'
        top_class = ''
        if date.month == 1:
            top_class = ' top-row'
        number = int(date.strftime("%d"))
        return '<div class="block{}{}"><div class="name">{}</div><div class="number">{}</div></div>'.format(weekend_class, top_class, date.strftime("%a").lower(), number)


    def month_cell(date):
        return '<div class="block"><div class="month">' + date.strftime("%b").lower() + '</div></div>'


    def empty_cell():
        return '<div class="block"></div>'


    def generate_month(m):
        days = [d for d in dates if d.month == m]
        str_formats = [day.strftime("%d") for day in days]
        str_formats.insert(0, days[0].strftime("%b"))
        str = ' & '.join(str_formats)
        cells = [date_to_cell(day) for day in days]
        cells.insert(0, month_cell(days[0]))
        if 32 - len(cells) > 0:
            padding = [empty_cell() for i in range(32 - len(cells))]
            cells = cells + padding
        return '\n'.join(cells)


    dates = []
    start_date = date(year, 1, 1)
    end_date = date(year + 1, 1, 1)
    for single_date in daterange(start_date, end_date):
        dates.append(single_date)

    html_string = '\n'.join([generate_month(i) for i in range(1,13)])
    header_string = '<h1 class="header">{}</h1>\n'.format(year)
    f = open('./index_template.html', 'r')
    lines = f.readlines()
    f.close()
    f = open('./index.html', 'w')
    for line in lines:
        if line == "year\n":
            line = header_string
        if line == "template\n":
            line = html_string
        f.write(line)
    f.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the year for which to generate the calendar")
        sys.exit(1)
    year = int(sys.argv[1])
    if year < 1970:
        print("Year should be larger than 1970")
        sys.exit(1)
    generate_calendar(int(sys.argv[1]))
