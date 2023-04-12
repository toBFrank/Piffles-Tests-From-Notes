################################################################################
# Title: Piffles - TxtConverter main
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
    file = input('Enter file name: ')
    
    # 2.0 Convert file
    converter = TxtConverter(file)
    converter.convert()
    

if __name__ == '__main__':
    main()