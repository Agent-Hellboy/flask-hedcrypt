"""
This module provide the APIs to insert the key inside the pdf file and to extract key from pdf.
Key should be the derived key using PKCS7 
"""

from PyPDF2 import PdfFileReader, PdfFileWriter


class FileHandler:
    """
	Attributes:
	key: derived key of the user.
	filename: filename of file in which key has to be inserted.

	"""

    def __init__(self, key, filename):
        self.key = key
        self.filename = filename

    def insert_key(self):
        """Insert derived key inside the PDF."""
        file_in = open(self.filename, "rb")
        pdf_reader = PdfFileReader(file_in)
        metadata = pdf_reader.getDocumentInfo()

        pdf_writer = PdfFileWriter()
        pdf_writer.appendPagesFromReader(pdf_reader)
        pdf_writer.addMetadata(
            {"/public_key": self.key,}
        )
        file_out = open(self.filename, "wb")
        pdf_writer.write(file_out)
        file_in.close()
        file_out.close()

    def get_key(self):
        """Extract keys from pdf."""
        try:
            file_in = open(self.filename, "rb")
            pdf_reader = PdfFileReader(file_in)
            metadata = pdf_reader.getDocumentInfo()
            public_key = metadata.get("/public_key")
        except FileNotFoundError:
            return None
        else:
            return public_key
