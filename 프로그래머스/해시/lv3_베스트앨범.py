# 장르별 전체 재생횟수에 대한 dict 생성
# 장르의 곡의 재생횟수에 대한 dict 생성
# 장르별 재생횟수로 우선순위 정하고 장르 내의 곡의 재생횟수에 따른 우선순위

def solution(genres, plays):
    answer = []
    genre_dict = dict()
    genre_playlist_dict = dict()
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genre_dict:
            genre_dict[genre] = play
            genre_playlist_dict[genre] = [(i, play)]
        else:
            genre_dict[genre] += play
            genre_playlist_dict[genre].append((i, play))
    genre_play_list = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(genre_play_list)):
        genre = genre_play_list[i][0]
        if len(genre_playlist_dict[genre]) <= 1:
            answer.append(genre_playlist_dict[genre][0][0])
        else:
            music_play_list = sorted(genre_playlist_dict[genre], key=lambda x:x[1], reverse=True)
            answer.append(music_play_list[0][0])
            answer.append(music_play_list[1][0])
    return answer