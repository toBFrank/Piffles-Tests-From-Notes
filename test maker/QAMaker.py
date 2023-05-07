################################################################################
# Title: Piffles - Question & Answer Maker
# Description: Use a text file to create a question and answer test.
# Author: Franco Bonilla
# Date: 2023-05-06
# Version: 1.0
################################################################################
import spacy

class QAMaker:
    def __init__(self, filename: str):
        self.filename = filename
        self.nlp_en = spacy.load("en_core_web_sm")

    def make_questions(self) -> None:
        '''
        Makes questions from a text file.

        Parameters - None
        Returns - None
        '''

        # 1.0 Get text
        with open(self.filename, "r") as f:
            text = f.read()
            text = text.replace("\n", "")
        
        # 2.0 Get sentences
        doc = self.nlp_en(text)
        sentences = [sent.text for sent in doc.sents]
        # print("QAMAKER - Sentences: ", sentences)

        # 3.0 Find 

def test():
    filename = "testQAMaker.txt"
    qa_maker = QAMaker(filename)
    qa_maker.make_questions()

if __name__ == "__main__":
    test()