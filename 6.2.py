scores = {
    1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
    2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
    3: ['Б', 'Г', 'Ё', 'Ь', 'Я'],
    4: ['Й', 'Ы'],
    5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
    8: ['Ш', 'Э', 'Ю'],
    10: ['Ф', 'Щ', 'Ъ'],
}

score = 0

word = input().upper()
for sym in word:
    for name in scores:
        if sym in scores[name]:
            score += name

print("Your score: " + str(score))