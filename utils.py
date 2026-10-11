def yes_or_no(value: bool):
    return "Да" if value else "Нет"

def print_summary(data_summary):
    print(
        f"""Город: {data_summary["city"]} 
Погода: {data_summary["weather"]["temp_c"]}°C 
Тёплая одежда: {yes_or_no(data_summary["weather"]["warm_clothes"])} 
{data_summary["rates"]["currency"]}→RUB: {data_summary["rates"]["rate_to_rub"]} 
Дорогой курс: {yes_or_no(data_summary["rates"]["expensive"])} """
    );