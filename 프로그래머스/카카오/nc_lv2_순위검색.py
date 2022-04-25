# 효율성 통과 X
# 해당 루프 넘어가려면 pass가 아닌 continue

def solution(info, query):
    info_dict = {i: {'lang': inf.split()[0], 'job': inf.split()[1], 'year': inf.split()[2], 'food': inf.split()[3], 'score': int(inf.split()[4])} for i, inf in enumerate(info)}
    query_dict = {i: {'lang': qu.split()[0], 'job': qu.split()[2], 'year': qu.split()[4], 'food': qu.split()[6], 'score': qu.split()[7]} for i, qu in enumerate(query)}
    answer = []
    for i in range(len(query)):
        ans = 0
        lang = query_dict[i]['lang']   
        job = query_dict[i]['job']
        year = query_dict[i]['year']
        food = query_dict[i]['food']
        score = query_dict[i]['score']
        for j in range(len(info)):
            if lang != '-':
                if info_dict[j]['lang'] != lang:
                    continue
            if job != '-':
                if info_dict[j]['job'] != job:
                    continue
            if year != '-':
                if info_dict[j]['year'] != year:
                    continue
            if food != '-':
                if info_dict[j]['food'] != food:
                    continue
            if score != '-':
                if info_dict[j]['score'] < int(score):
                    continue
            ans += 1
        answer.append(ans)
    return answer