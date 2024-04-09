from django.shortcuts import render
from datetime import date, datetime


# main page of first app
def main(request):
    context = {
        "str_join": ["a", "b", "c", "d"],
        "add_some": [1, 2, 3, 4, 5, 6],
        "cut_some": "january - february - march",
        "dist_sort": [
            {"name": "Josh", "age": 19},
            {"name": "Dave", "age": 22},
            {"name": "Joe", "age": 31},
        ],
        "lower": "I am a hero",
        "date": date.today(),
        "time": datetime.now(),
    }

    return render(request, "first_app/index.html", context)
