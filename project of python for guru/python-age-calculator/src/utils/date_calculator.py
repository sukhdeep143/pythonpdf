def calculate_age(birth_date):
    from datetime import datetime, timedelta

    today = datetime.now()
    age_in_days = (today - birth_date).days
    age_in_years = age_in_days // 365
    age_in_days %= 365
    age_in_hours = age_in_days * 24
    age_in_minutes = age_in_hours * 60
    age_in_seconds = age_in_minutes * 60

    return age_in_years, age_in_days, age_in_minutes, age_in_seconds

def parse_date(date_string):
    from datetime import datetime

    return datetime.strptime(date_string, "%Y-%m-%d")