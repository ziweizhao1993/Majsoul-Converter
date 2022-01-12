#Based on https://lions-blue.hatenablog.jp/entry/2021/10/23/191220
#Coded by zzw (我爱豆腐)
import json
import sys

qh_paipu_name = "1_11_2022_Jade_Room_South.json"
th_paipu_name = "output.json"

hand_dict = {
    "Mangan": "満貫",
    "Haneman": "跳満",
    "Baiman": "倍満",
    "Sanbaiman": "三倍満",
    "Yakuman": "役満",
    "Kazoeyakuman": "数え役満",
    "Kiriagemangan": "切り上げ満貫"
}

yaku_dict = {
    "White Dragon": "役牌 白",
    "Green Dragon": "役牌 發",
    "Red Dragon": "役牌 發",
    "Ura Dora": "",
    "Riichi": ""
}

ending_dict = {
    "Ryuukyoku":"流局"
}
def get_th_title(qh_title):
    room_name = qh_title[0].split(' ')[0]
    game_length = qh_title[0].split(' ')[2]
    game_date = qh_title[1]

    if room_name == "Bronze":
        room = "铜之间"
    elif room_name == "Silver":
        room = "银之间"
    elif room_name == "Gold":
        room = "金之间"
    elif room_name == "Jade":
        room = "玉之间"
    elif room_name == "Throne":
        room = "王座之间"
    else:
        room = "？之间"

    if game_length == "South":
        length = "四人南"
    elif game_length == "East":
        length = "四人东"
    
    return ([room+length, game_date])
    
def get_th_log(qh_log):
#Basically changing english names to japanese names
    #print (qh_log)
    #dict:

    #special endings
    if qh_log[-1][0] in ending_dict.keys():
        qh_log[-1][0] = ending_dict[qh_log[-1][0]]
        return ([qh_log])

    print (qh_log[-1][2][3].split(' ')[0])
    if qh_log[-1][2][3].split(' ')[0] in hand_dict.keys():
        qh_log[-1][2][3] = hand_dict[qh_log[-1][2][3].split(' ')[0]]+qh_log[-1][2][3].split(' ')[1]

    return ([qh_log])

with open(qh_paipu_name, 'r') as f:
    #To remove \n from json file
    qh_paipu = ''.join(f.readlines())
    qh_paipu = json.loads(qh_paipu)

th_paipu = {}
th_paipu["title"] = get_th_title(qh_paipu["title"])
th_paipu["name"] = qh_paipu["name"]
th_paipu["rule"] = qh_paipu["rule"]

with open(qh_paipu_name[:-5]+"_th"+".txt", 'w') as f:
    for i in range(len(qh_paipu["log"])):
        th_paipu["log"] = get_th_log(qh_paipu["log"][i])
        th_paipu_line = 'https://tenhou.net/6/#json=' + json.dumps(th_paipu, ensure_ascii = False , separators = ( ',' , ':' ))
        f.write (th_paipu_line+'\n')
