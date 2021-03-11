def Numer0n():
    print('ヌメロンを始めます！！')
    input('3桁の数字を入力してください')

    return


def return_message(message):
    if message=='ヌメロン' or message=='ぬめろん' or message=='Numer0n':
        returnMessage = 'Numer0n開始'
    elif message=='今日の高速道路' or message=='高速道路':
        returnMessage = '今日おすすめの高速道路は...東名高速！！'
    elif message=='今日の麺類' or message=='麺類':
        returnMessage = '今日おすすめの麺類は...日高屋のチゲ味噌ラーメン！！'
    else:
        returnMessage = 'YO!YO!' + message + 'だYo！'

    return returnMessage