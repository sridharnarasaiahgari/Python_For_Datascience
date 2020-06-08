## 1. If Statements ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price == 0.0:
        free_apps_ratings.append(rating)
avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)

## 2. Booleans ##

a_price = 0
if a_price == 0:
    print('This is free')
if a_price == 1:
    print('This is not free')

## 3. The Average Rating of Non-free Apps ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price != 0.0:
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

## 4. The Average Rating of Gaming Apps ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
non_games_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if genre != 'Games':
        non_games_ratings.append(rating)
        
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)

## 5. Multiple Conditions ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    if price == 0 and genre == 'Games':
        free_games_ratings.append(rating)
        
avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)

## 6. The or Operator ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if genre == 'Games' or genre == 'Social Networking':
        games_social_ratings.append(rating)
        
avg_games_social = sum(games_social_ratings) / len(games_social_ratings)

## 7. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        free_games_social_ratings.append(rating)
        
avg_non_free = sum(free_games_social_ratings) / len(free_games_social_ratings)

# Non-free apps (average)

## 8. Comparison Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

app_price_gt_9 = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    
    if price > 9:
        app_price_gt_9.append(rating)
        
avg_rating = sum(app_price_gt_9) / len(app_price_gt_9)
n_apps_more_9 = len(app_price_gt_9) 
n_apps_less_9 = len(apps_data[1:]) - n_apps_more_9



## 9. The else Clause ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0:
        app.append('free')
    else:
        app.append('non-free')
apps_data[0].append('free_or_not')
print(apps_data[1])
print(apps_data[1:7])

## 10. The elif Clause ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0:
        app.append('free')
    elif price > 0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    elif price >=50:
        app.append('very expensive')
apps_data[0].append('price_label')
print(apps_data[0])
print(apps_data[1:7])