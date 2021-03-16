import random

def Numer0n():
    print('ヌメロンを始めます！！')
    my_number = input('3桁の数字を入力してください(同じ数字はNG):')
    print(my_number)

    return my_number


def return_message(message):
    if message=='ヌメロン' or message=='ぬめろん' or message=='Numer0n':
        returnMessage = 'Numer0n開始'
    elif message=='今日の高速道路' or message=='高速道路':
        returnMessage = '今日おすすめの高速道路は...東名高速！！'
    elif message=='今日の麺類' or message=='麺類':
        returnMessage = '今日おすすめの麺類は...日高屋のチゲ味噌ラーメン！！'
    elif '日向坂' in message:
        returnMessage = 'メンバーを入力して下さい\n'.join(hnt_list('name'))
    
    else:
        returnMessage = 'YO!YO!' + message + 'だYo！'

    return returnMessage

def hnt_list(select):
    if select == 'name':
        hnt_list = [
            '佐々木久美',
            '佐々木美鈴',
            '斎藤京子',
            '高本彩花',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
        ] 
    elif select == 'message':
        hnt_list = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
        ]
    return hnt_list