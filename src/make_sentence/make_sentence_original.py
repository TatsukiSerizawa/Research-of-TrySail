import markov

with open('../../data/blog/Natukawa_Shiina/cleaning_text.txt') as f:
    text = f.read()

text_model = markov.Text(text)

for i in range(10):
    print(text_model.make_sentence())