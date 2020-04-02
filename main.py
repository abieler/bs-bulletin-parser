import argparse
import logging

logging.basicConfig(level=logging.INFO)

import spacy



def replace_numberwords(text: str) -> str:
    return " ".join([numbermapping.get(word.strip(".,:;"), word) for word in text.split(" ")])


def preprocess(text: str) -> str:
    text = text.replace(",", "").replace("\n", " ")
    return replace_numberwords(text)


def parse(text: str) -> dict:
    result = {}
    nlp = spacy.load("nlp")
    doc = nlp(text)
    for sent in doc.sents:
        sdoc = nlp(sent.string.strip())
        for ent in sdoc.ents:
            try:
                result[ent.label_] = int(ent.text.strip('.,'))
            except ValueError:
                logging.warning(f"Error parsing: {ent.text.strip('.,')}")
    return result


def update_indirect_numbers(result: dict) -> dict:
    if result.get("NUMCUL_CONF", None) and result.get("NUMCUL_CONF_RESIDENTS"):
        result["NCUMUL_CONFIRMED_NON_RESIDENT"] = result["NUMCUL_CONF"] - result["NUMCUL_CONF_RESIDENTS"]

    if result.get("NUMCUL_HOSP", None) and result.get("NUMCUL_HOSP_RESIDENTS", None):
        result["NINST_HOSP_NON_RESIDENT"] = result["NUMCUL_HOSP"] - result["NUMCUL_HOSP_RESIDENTS"]

    return result




with open("numbers.txt", "r") as txtfile:
    numbermapping = {l.strip(): str(i) for i, l in enumerate(txtfile.readlines())}
numbermapping["hundert"] = "100"
numbermapping["tausend"] = "1000"
numbermapping["einen"] = "1"
numbermapping["eine"] = "1"
numbermapping["eins"] = "1"



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", type=str)
    args = parser.parse_args()

    with open(args.filename, "r") as txtfile:
        text = txtfile.read()

    ptext = preprocess(text)
    result = parse(ptext)
    result = update_indirect_numbers(result)

    for k, v in result.items():
        print(f"{k:30}: {v}")
