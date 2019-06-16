
@staticmethod
def trim(raw_text):
    return raw_text.strip().replace(",", "").replace("\n","").replace("\t","")