# import spacy
# nlp = spacy.load("es_core_news_lg")


# textos = "El gerente de la sucursal de Gama en Macaraycuay estaba muy emocionado por el lanzamiento de su nueva línea de productos gourmet. Él y su equipo habían trabajado incansablemente para asegurarse de que todo estuviera listo para el gran día. Como parte de la celebración, invitaron a un famoso charcutero para que hiciera una demostración en vivo de cómo hacer salchichas y otros productos cárnicos. La multitud se reunió en la sucursal de Gama para probar los deliciosos manjares y disfrutar de la música en vivo. Al final del día, el gerente estaba agradecido con su equipo y con los clientes de la sucursal de Macaraycuay por su apoyo y lealtad a la marca Gama."
# texto2 = "el gama tiene una gama alta de procutos"

# doc = nlp(textos)
# ruler = nlp.add_pipe("entity_ruler")
# patterns = [{"label": "ORG", "pattern": [{"lower": "gama"}]},
#             {"label": "CARG", "pattern": [{"lower": "gerente"}]},
#             {"label": "CARG", "pattern": [{"lower": "charcutero"}]},
#             {"label": "LOC", "pattern": [{"lower": "Macaraycuay"}]}]

# ruler.add_patterns(patterns)
# doc = nlp(texto2)

# for ents in doc.ents:
#     if ents.label_ == 'ORG' or ents.label_ == 'CARG' or ents.label_ == 'LOC':
#         print(ents.text, ents.label_,)


# # for ent in doc.ents:
# #     print(ent.text, ent.label_)


import spacy
nlp = spacy.load("es_core_news_lg")


textos = "El Gerente de la sucursal de gama en Macaraycuay estaba muy emocionado por el lanzamiento de su nueva línea de productos gourmet. Él y su equipo habían trabajado incansablemente para asegurarse de que todo estuviera listo para el gran día. Como parte de la celebración, invitaron a un famoso charcutero para que hiciera una demostración en vivo de cómo hacer salchichas y otros productos cárnicos. La multitud se reunió en la sucursal de Gama para probar los deliciosos manjares y disfrutar de la música en vivo. Al final del día, el gerente estaba agradecido con su equipo y con los clientes de la sucursal de Macaraycuay por su apoyo y lealtad a la marca Gama."

corpus = []

doc = nlp(textos)

for sent in doc.sents:
    corpus.append(sent.text)

nlp = spacy.blank("es")

ruler = nlp.add_pipe("entity_ruler")

patterns = [{"label": "ORG", "pattern": [{"lower": "gama"}]},
            {"label": "CARG", "pattern": [{"lower": "gerente"}]},
            {"label": "CARG", "pattern": [{"lower": "charcutero"}]},
            {"label": "LOC", "pattern": [{"lower": "macaraycuay"}]},
            {"label": "LOC", "pattern": [{"lower": "tahona"}]},
            {"label": "LOC", "pattern": [{"lower": "trinidad"}]}]

ruler.add_patterns(patterns)


TRAIN_DATA = []


for sentences in corpus:
    doc = nlp(sentences)

    entities = []

    for ent in doc.ents:

        entities.append([ent.start_char, ent.end_char, ent.label_])

    TRAIN_DATA.append([sentences, {"entities": entities}])

print (TRAIN_DATA)