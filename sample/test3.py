# link = input("URL: ")
#
# if link.startswith("https://") or link.startswith("http://"):
#     print(f"{link}は有効なリンクです")
# else:
#     print(f"{link}は無効なリンクです")

# 基数を入力
baseNum = int(input("変換先の基数を入力してください: "))
while True:
    if baseNum in {2, 8, 10, 16}:
        break
    else:
        baseNum = int(input("再入力をお願いします: "))

# 変換する数値
inputNum = int(input("変換する数値を入力してください: "))

if baseNum == 2:
    print("aaa")