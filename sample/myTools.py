# 確認するあれ
def confirm():
    check = input("確定しますか?(Y/n): ")
    if check == 'Y' or check == 'y':
        state = True
    elif check == 'n' or check == 'N':
        state = False
    return state
