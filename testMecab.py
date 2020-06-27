import MeCab

m = MeCab.Tagger("-d /usr/lib64/mecab/dic/mecab-ipadic-neologd -Owakati")

print(m.parse("彼女はペンパイナッポーアッポーペンと恋ダンスを踊った。"))
