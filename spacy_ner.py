import json


import spacy


def _get_spacy_pipe(lang_code: str):
    model_code = f"{lang_code}_core_news_sm"
    try:
        pipe = spacy.load(model_code)
    except:
        spacy.cli.download(model_code)
        pipe = spacy.load(model_code)
    return pipe


def _get_entities(doc):
    entities = []
    for entity in doc.ents:
        start = entity.start_char
        end = entity.end_char
        category = entity.label_
        text = entity.text
        entity = {
                   "text": text,
                    "type": category,
                    "start_pos": start,
                    "end_pos": end
        }
        entities.append(entity)
    return entities


def ner(text: str, language_code: str):
    pipe = _get_spacy_pipe(lang_code=language_code)
    doc = pipe(text)
    return _get_entities(doc=doc)


if __name__ == "__main__":
    entities = ner("Lubię firmę Apple", "pl")
    print(json.dumps(entities, indent=4))

