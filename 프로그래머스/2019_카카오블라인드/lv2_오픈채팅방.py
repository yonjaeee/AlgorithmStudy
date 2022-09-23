def solution(record):
    answer = []
    uid_list = []
    uid_name_dict = dict()
    for i in range(len(record)):
        r = record[i].split()
        if r[0] == 'Enter':
            uid_name_dict[r[1]] = r[2]
            uid_list.append(r[1])
            answer.append("님이 들어왔습니다.")
        elif r[0] == 'Change':
            uid_name_dict[r[1]] = r[2]
        else:
            uid_list.append(r[1])
            answer.append("님이 나갔습니다.")
    name_list = [uid_name_dict[uid] for uid in uid_list]
    result = list(zip(name_list, answer))
    result = [''.join(x) for x in result]
    return result