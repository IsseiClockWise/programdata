import random
marks = ['club','diamond','heart','spade']
numbers = range(1,14)
cards = [(i,j) for i in marks for j in numbers]
card_count = 0
random.shuffle(cards)
win_count = 0.0
judge_count = 0
while card_count < len(cards) - 1:
    open_card = cards[card_count][1]
    print('High and Low ゲームスタート!!')
    while True:
        print('現在のカードは{}です'.format(open_card))
        print('次のカードの数字を　High:1 Low:2 で予測してください')
        answer = input()    
        if answer == '1' or answer == '2': break
    card_count += 1
    answer_card = cards[card_count][1]
    print('カードの値は、{}です！'.format(answer_card))
    if open_card < answer_card:
        print('正解はHighでした！')
        if answer == '1':
            print('お見事！正解です！')
            win_count += 1
        elif answer == '2':
            print('残念！不正解です！')
        judge_count += 1
    elif open_card > answer_card:
        print('正解はLowでした！')
        if answer == '2':
            print('お見事！正解です！')
            win_count += 1
        elif answer == '1':
            print('残念！不正解です！')
        judge_count += 1
    else:
        print('同じ値でした！勝敗には関係ありません！')
    if judge_count == 0 or win_count == 0:
        print('現在の勝率は{}%です。'.format(0))
    else:
        print('現在の勝率は{}%です。'.format((win_count/judge_count)*100))
print('カードがきれたためゲーム終了です')
