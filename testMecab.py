import os
import MeCab

dict_path = os.getenv("MECAB_DICTIONARY_PATH", "/usr/lib64/mecab/dic/mecab-ipadic-neologd")
m = MeCab.Tagger(f"-d {dict_path} -Owakati")

print(m.parse("彼女はペンパイナッポーアッポーペンと恋ダンスを踊った。"))
