################################################################################
# Title: Piffles - TxtConverter Question maker
# Description: Converts raw files (.pdf) to text files.
# Author: Franco Bonilla
# Date: 2023-04-11
# Version: 1.0
################################################################################
from TxtConverter import TxtConverter



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

    # 3.0 Get key words/concepts
    # natLangProccessor = NatLangProcessor(self.file.split('.')[0] + '.txt')
    

if __name__ == '__main__':
    main()