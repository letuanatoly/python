#Имеется 100 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги,
# если плата за быка – 10 рублей, за корову – 5 рублей,
# за телёнка – 0.5 рубля и надо купить 100 голов скота?
total = 0
for bulls in range(1, 11):
    for cows in range(1, 21):
        for calfs in range(1, 201):
            if 10 * bulls + 5 * cows + 0.5 * calfs == 100 and bulls + cows + calfs == 100:
                print('Быки: ', bulls, ', коровы: ', cows, ', телята: ', calfs, sep='')
                total += 1
print('Общее количество решений:', total)