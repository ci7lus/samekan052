import os
import markovify
import MeCab

try:
    dict_path = os.getenv("MECAB_DICTIONARY_PATH", "/usr/lib64/mecab/dic/mecab-ipadic-neologd")
    m = MeCab.Tagger(f"-d {dict_path} -Owakati")
except Exception as e:
    m = MeCab.Tagger("-Owakati")


with open("tweets.txt", "r") as f:
    data = f.read()

corpus = "".join([m.parse(s) for s in data.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace(
    "?", "？").replace("!", "！").replace("，", "、").replace("．", "。").replace("。", "。\n")
    .split("\n") if s != ""])
model = markovify.NewlineText(corpus, state_size=3).to_json()

with open("dist/model.json", "w") as f:
    f.write(model)
