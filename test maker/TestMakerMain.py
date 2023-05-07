################################################################################
# Title: Piffles - Test Maker Main
# Description: Converts raw files (.pdf) to text files.
# Author: Franco Bonilla
# Date: 2023-04-11
# Version: 1.0
################################################################################
from TxtConverter import TxtConverter
from QAMaker import QAMaker



def main() -> None:
    '''
    Main function of the program.
    
    Parameters - None
    Returns - None
    '''
    # 1.0 Get file name
    filename = input('Enter file name: ')
    
    # 2.0 Convert file
    converter = TxtConverter()
    filename_txt = converter.convert(filename)

    # 3.0 Make questions and answers
    qa_maker = QAMaker(filename_txt)
    
    

if __name__ == '__main__':
    main()