from prettytable import PrettyTable

data = [
    {"name": "Cristiano Ronaldo", "follower_count": 1500000, "description": "Footballer", "country": "Portugal"},
    {"name": "Ariana Grande", "follower_count": 1400000, "description": "Singer", "country": "USA"},
    {"name": "Dwayne Johnson", "follower_count": 1300000, "description": "Actor", "country": "USA"},
    {"name": "Kylie Jenner", "follower_count": 1200000, "description": "Entrepreneur", "country": "USA"},
    {"name": "Selena Gomez", "follower_count": 1100000, "description": "Singer", "country": "USA"},
    {"name": "Kim Kardashian", "follower_count": 1000000, "description": "TV Personality", "country": "USA"},
    {"name": "Lionel Messi", "follower_count": 950000, "description": "Footballer", "country": "Argentina"},
    {"name": "Beyoncé", "follower_count": 900000, "description": "Singer", "country": "USA"},
    {"name": "Justin Bieber", "follower_count": 850000, "description": "Singer", "country": "Canada"},
    {"name": "Taylor Swift", "follower_count": 800000, "description": "Singer", "country": "USA"},
    {"name": "Neymar Jr.", "follower_count": 750000, "description": "Footballer", "country": "Brazil"},
    {"name": "Kendall Jenner", "follower_count": 700000, "description": "Model", "country": "USA"},
    {"name": "Khloé Kardashian", "follower_count": 650000, "description": "TV Personality", "country": "USA"},
    {"name": "Nicki Minaj", "follower_count": 600000, "description": "Rapper", "country": "USA"},
    {"name": "Jennifer Lopez", "follower_count": 550000, "description": "Singer", "country": "USA"},
    {"name": "Miley Cyrus", "follower_count": 500000, "description": "Singer", "country": "USA"},
    {"name": "Kourtney Kardashian", "follower_count": 450000, "description": "TV Personality", "country": "USA"},
    {"name": "Kevin Hart", "follower_count": 400000, "description": "Comedian", "country": "USA"},
    {"name": "Cardi B", "follower_count": 350000, "description": "Rapper", "country": "USA"},
    {"name": "LeBron James", "follower_count": 300000, "description": "Basketball Player", "country": "USA"},
    {"name": "Billie Eilish", "follower_count": 250000, "description": "Singer", "country": "USA"},
    {"name": "Shakira", "follower_count": 200000, "description": "Singer", "country": "Colombia"},
    {"name": "Chris Hemsworth", "follower_count": 150000, "description": "Actor", "country": "Australia"},
    {"name": "Zendaya", "follower_count": 100000, "description": "Actress", "country": "USA"},
    {"name": "Tom Holland", "follower_count": 95000, "description": "Actor", "country": "UK"},
    {"name": "Priyanka Chopra", "follower_count": 90000, "description": "Actress", "country": "India"},
    {"name": "Shawn Mendes", "follower_count": 85000, "description": "Singer", "country": "Canada"},
    {"name": "Emma Watson", "follower_count": 80000, "description": "Actress", "country": "UK"},
    {"name": "Gal Gadot", "follower_count": 75000, "description": "Actress", "country": "Israel"},
    {"name": "Will Smith", "follower_count": 70000, "description": "Actor", "country": "USA"},
    {"name": "Rihanna", "follower_count": 65000, "description": "Singer", "country": "Barbados"},
    {"name": "Gigi Hadid", "follower_count": 60000, "description": "Model", "country": "USA"},
    {"name": "Zayn Malik", "follower_count": 55000, "description": "Singer", "country": "UK"},
    {"name": "Hugh Jackman", "follower_count": 50000, "description": "Actor", "country": "Australia"},
    {"name": "Chris Evans", "follower_count": 45000, "description": "Actor", "country": "USA"},
    {"name": "Bruno Mars", "follower_count": 40000, "description": "Singer", "country": "USA"},
    {"name": "Dua Lipa", "follower_count": 35000, "description": "Singer", "country": "UK"},
    {"name": "Vin Diesel", "follower_count": 30000, "description": "Actor", "country": "USA"},
    {"name": "Jason Momoa", "follower_count": 25000, "description": "Actor", "country": "USA"},
    {"name": "Sophie Turner", "follower_count": 20000, "description": "Actress", "country": "UK"},
    {"name": "Millie Bobby Brown", "follower_count": 15000, "description": "Actress", "country": "UK"},
    {"name": "Henry Cavill", "follower_count": 10000, "description": "Actor", "country": "UK"},
    {"name": "Camila Cabello", "follower_count": 9500, "description": "Singer", "country": "USA"},
    {"name": "Liam Hemsworth", "follower_count": 9000, "description": "Actor", "country": "Australia"},
    {"name": "Margot Robbie", "follower_count": 8500, "description": "Actress", "country": "Australia"},
    {"name": "Shawn Mendes", "follower_count": 8000, "description": "Singer", "country": "Canada"},
    {"name": "Anya Taylor-Joy", "follower_count": 7500, "description": "Actress", "country": "USA"},
    {"name": "Timothée Chalamet", "follower_count": 7000, "description": "Actor", "country": "USA"},
    {"name": "Zendaya", "follower_count": 6500, "description": "Actress", "country": "USA"}
]

table = PrettyTable()
table.field_names = ["Name", "Follower Count", "Description", "Country"]

for entry in data:
    table.add_row([
        entry["name"], 
        entry["follower_count"], 
        entry["description"], 
        entry["country"]])
print(table)