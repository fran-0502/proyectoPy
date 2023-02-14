import spacy
import pandas as pd
from spacy.tokens import DocBin
from datetime import datetime
nlp = spacy.load('es_core_news_lg')


data_frame = pd.read_csv(
    "betsentiment-ES-tweets-sentiment-teams.csv", encoding="latin-1")


# data_frame.head()
# data_frame["tweet_text"][0]
data_frame.shape

entrenamiento = data_frame.sample(frac=0.8, random_state=25)
prueba = data_frame.drop(entrenamiento.index)

# print(entrenamiento.shape, prueba.shape)

entrenamiento['tuples'] = entrenamiento.apply(
    lambda row: (row['tweet_text'], row['sentiment']), axis=1)

entrenamiento = entrenamiento['tuples'].tolist()

prueba['tuples'] = prueba.apply(
    lambda row: (row['tweet_text'], row['sentiment']), axis=1)


def document(data):
    # Creating empty list called "text"
    text = []
    for doc, label in nlp.pipe(data, as_tuples=True):
        if (label == 'POSITIVE'):
            doc.cats['POSITIVE'] = 1
            doc.cats['NEGATIVE'] = 0
            doc.cats['NEUTRAL'] = 0
        elif (label == 'NEGATIVE'):
            doc.cats['POSITIVE'] = 0
            doc.cats['NEGATIVE'] = 1
            doc.cats['NEUTRAL'] = 0
        else:
            doc.cats['POSITIVE'] = 0
            doc.cats['negative'] = 0
            doc.cats['NEUTRAL'] = 1
# Adding the doc into the list 'text'
            text.append(doc)
    return (text)


start_time = datetime.now()
train_docs = document(entrenamiento)
doc_bin = DocBin(docs=train_docs)
doc_bin.to_disk("train.spacy")
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# start_time = datetime.now()
# test_docs = document(prueba)
# doc_bin = DocBin(docs=test_docs)
# doc_bin.to_disk("test.spacy")
# end_time = datetime.now()
# print('Duration: {}'.format(end_time - start_time))
