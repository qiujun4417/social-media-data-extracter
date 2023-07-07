from datetime import datetime

def time_formatter(time_str):
    date = datetime.strptime(time_str, '%a %b %d %H:%M:%S %z %Y')
    formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date