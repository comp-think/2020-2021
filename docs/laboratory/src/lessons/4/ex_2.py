lyrics = "well i’m so above you ;; and it’s plain to see ;; but i came to love you anyway ;; so you pulled my heart out ;; and i don’t mind bleeding ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; well your mama kept you but your daddy left you ;; and i should’ve done you just the same ;; but i came to love you ;; am i born to bleed? ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; hey! ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting"

#----(a)
def count_words(txt_lyrics):
    result_dict = {}
    lyrics_l = txt_lyrics.split(" ")
    unwated_list = ['', 'a', 'i', 'am', 'to', ';;', 'the', 'you', 'don’t', 'and', 'that', 'i’m', 'it’s']
    for w in lyrics_l:
        if w not in unwated_list:
            if w not in result_dict:
                result_dict[w] = 0
            result_dict[w] += 1

    return result_dict

count_dict = count_words(lyrics)
print(count_dict)

#----(b)
playlist_txt = "el_camino::lonely_boy ;; el_camino::little_black_submarine ;; el_camino::gold_on_the_ceiling ;; turn_blue::fever ;; turn_blue::gotta_get_away ;; brothers::howlin_for_you ;; brothers::tighten_up ;; turn_blue::it_is_up_to_you_now"

def build_playlist_dict(a_txt):
    result_dict = {}
    songs = a_txt.split(" ;; ")
    for a_song in songs:
        song_parts = a_song.split("::")
        album = song_parts[0]
        song_name = song_parts[1]
        if album not in result_dict:
            result_dict[album] = []
        result_dict[album].append(song_name)
    return result_dict

print(build_playlist_dict(playlist_txt))
