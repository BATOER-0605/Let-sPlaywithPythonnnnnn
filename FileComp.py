import sys

#文字コードが起因のエラー対策
defaultencoding = sys.getdefaultencoding()

#ファイルの読み込みとエラー処理
inport1 =input("1つ目のファイル名\n")
inport2 =input("2つ目のファイル名\n")

try:
    with open(inport1,'r',encoding=defaultencoding) as file1:
        f1=file1.read()

except FileNotFoundError:
    print("ファイルが存在しません: 1つ目のファイル\n")
    exit()

try:
    with open(inport2,'r',encoding=defaultencoding) as file2:
        f2=file2.read()

except FileNotFoundError:
    print("ファイルが存在しません: 2つ目のファイル\n")
    exit()


#記載内容の比較
if(f1 == f2):
    print("ファイルの内容は同じです\n")

elif(f1 != f2):
    print("ファイルの記載内容は異なっています。\n")

else:
    print("エラーが出ました。\n")


print("1つ目のファイルの記載内容\n"+f1+"\n\n")
print("2つ目のファイルの記載内容\n"+f2+"\n\n")