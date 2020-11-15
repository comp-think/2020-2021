lyrics = "well i’m so above you ;; and it’s plain to see ;; but i came to love you anyway ;; so you pulled my heart out ;; and i don’t mind bleeding ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; well your mama kept you but your daddy left you ;; and i should’ve done you just the same ;; but i came to love you ;; am i born to bleed? ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; hey! ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting"

#----(a)
def clean_lyrics(txt_lyrics):
    lyrics_set = set(txt_lyrics.split(" "))
    unwated_list = ['', 'a', 'i', 'am', 'to', ';;', 'the', 'you', 'don’t', 'and', 'that', 'i’m', 'it’s']
    unwanted_set = set(unwated_list)
    clean_set = lyrics_set.difference(unwanted_set)
    return clean_set

my_set = clean_lyrics(lyrics)
print(my_set)

#----(b)
def common_words(clean_set):
    l_words = ["mama","daddy","sister","brother","boy","girl"]
    s_words = set(l_words)
    common_set = clean_set.intersection(s_words)
    return len(common_set)
    
print(common_words(my_set))
