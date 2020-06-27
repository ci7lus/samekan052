import markovify

with open("dist/model.json", "r") as f:
    textModel = markovify.Text.from_json(f.read())

while True:
    made = textModel.make_sentence(tries=100)

    if made:
        sentence = "".join(made.split())
        break

print(sentence)
