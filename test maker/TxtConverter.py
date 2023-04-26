################################################################################
# Title: Piffles - TxtConverter class
# Description: Converts raw files (.pdf) to text files.
# Author: Franco Bonilla
# Date: 2023-04-11
# Version: 1.0
################################################################################
import pypdf


class TxtConverter:
    def __init__(self):
        self.supported_file_types = ["pdf"]

    def convert(self, filename: str) -> str:
        """
        Extracts text from a file and returns it as a string.

        Parameters - None
        Returns - filename_txt: str of the name of the .txt file
        """
        file_type = filename.split(".")[-1]
        if file_type not in self.supported_file_types:
            raise ValueError(
                f"File type not supported. Supported file types: {self.supported_file_types}"
            )

        # 1.0 Get list of dirty text
        if file_type == "pdf":
            dirty_list = self._convert_pdf(filename)
        elif file_type == "ppt":
            dirty_list = self._convert_ppt(filename)

        # 2.0 Write to .txt file
        filename_txt = self._make_txt_file(dirty_list, filename)

        return filename_txt

    def _convert_pdf(self, filename: str) -> list[str]:
        """
        Extracts text from a pdf file and returns it as a string.

        Parameters - None
        Returns - dirty_list: list[str]
        """
        dirty_list = []
        dirty_pdf = pypdf.PdfReader(filename)

        # 1.1 Get pdf info
        pdf_info = dirty_pdf.metadata
        num_pages = len(dirty_pdf.pages)
        pdf_info_str = (
            f"| {filename} | Details\n"
            f"Author: {pdf_info.author}\n"
            f"Creator: {pdf_info.creator}\n"
            f"Producer: {pdf_info.producer}\n"
            f"Subject: {pdf_info.subject}\n"
            f"Title: {pdf_info.title}\n"
            f"Number of Pages: {num_pages}\n"
        )
        dirty_list.append(pdf_info_str)

        # 1.2 Get pdf text
        for page in dirty_pdf.pages:
            dirty_list.append(page.extract_text())
        # print(dirty_list)

        return dirty_list

    def _convert_ppt(self, filename: str) -> list[str]:
        """
        Extracts text from a ppt file and returns it as a string.

        Parameters - None
        Returns - dirty_list: list[str]
        """
        raise NotImplementedError("Coming soon!")

    def _make_txt_file(self, dirty_list: list[str], filename: str) -> str:
        """
        Writes a list of strings to a .txt file.

        Parameters - dirty_list: list[str]
        Returns - None
        """
        # 1.0 Get file name
        file_name = filename[:-4] + ".txt"

        # 2.0 Write to .txt file
        with open(file_name, "w", encoding="utf-8") as f:
            for item in dirty_list:
                f.write(item)
                f.write("\n")
        print(f"File saved as {file_name}.")

        return file_name