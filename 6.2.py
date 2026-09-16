seconds = int(input())

days, remainder = divmod(seconds, 24 * 60 * 60)
hours, remainder = divmod(remainder, 60 * 60)
minutes, seconds = divmod(remainder, 60)

if days == 1:
    day_word = "день"
elif 2 <= days <= 4:
    day_word = "дня"
else:
    day_word = "дней"

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")