import random

def Numer0n():
    print('ヌメロンを始めます！！')
    my_number = input('3桁の数字を入力してください(同じ数字はNG):')
    print(my_number)

    return my_number


def return_message(message):
    text_message = []
    if message=='ヌメロン' or message=='ぬめろん' or message=='Numer0n':
        text_message.append('Numer0n開始')
    elif message=='今日の高速道路' or message=='高速道路':
        text_message.append('今日おすすめの高速道路は...東名高速！！')
    elif message=='今日の麺類' or message=='麺類':
        text_message.append('今日おすすめの麺類は...日高屋のチゲ味噌ラーメン！！')
    elif '日向坂' in message:
        text_message.append('メンバーを入力して下さい')
        text_message.append('\n'.join(hnt_list('name')))
        # returnMessage = [TextSendMessage(text=text_message[0]), TextSendMessage(text=text_message[1])]
        # returnMessage = 'メンバーを入力して下さい\n'+'\n'.join(hnt_list('name'))
    
    else:
        text_message.append('YO!YO!' + message + 'だYo！')


    return text_message

def hnt_list(select):
    if select == 'name':
        hnt_list = [
            '佐々木久美',
            '佐々木美鈴',
            '斎藤京子',
            '高本彩花',
            '高瀬愛奈',
            '潮紗理奈',
            '東村芽依',
            '加藤史帆',
            '影山優佳',
            '丹生明里',
            '宮田愛萌',
            '濱岸ひより',
            '河田陽菜',
            '松田好花',
            '富田鈴花',
            '渡邉美穂',
            '金村美玖',
            '小坂菜緒',
            '上村ひなの',
            '高橋未来虹',
            '山口陽世',
            '森本茉莉',
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