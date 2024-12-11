import random


def check(numb):
    while True:
        try:
            numb in znach
            int(numb)
        except (ValueError, AttributeError):
            numb = input('Ты ввел чтото не то .·´¯`(>▂<)´¯`·. попробуй еще раз (>' - '<) ')

znach = '123'







N = random.randint(4, 30)
print('В начальной куче', N, 'камней (。・ω・。) ')
move = 0

while N != 1:
    player_rok = input('Ваш ход, выберете сколько камней вы хотите убрать из кучи, 1, 2 или 3 o(〃＾▽＾〃)o ')
    player_rok = check(player_rok)

    N = N - player_rok
    if N == 1:
        break
    print('Осталось', N, 'камней, ты близок к победе ( •̀ ω •́ )✧ ')
    move += 1
    cyborg = random.randint(1, 3)
    N = N - cyborg
    print('Ход робота (⌐■_■)', cyborg)
    print('Осталось', N, 'камней, какой коварный ход (►__◄) ')
    move += 1
if move % 2 != 0:
    print('Ураааа, вы победили＼(ﾟｰﾟ＼) ( ﾉ ﾟｰﾟ)ﾉ ')
else:
    print('Эх, порожение ≧ ﹏ ≦ ну ничего, в другой раз все получится (づ￣ 3￣)づ ')
