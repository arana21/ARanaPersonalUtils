"""
This file contains functionality to file IO operations.
"""


import io
import json
import os


class BasicFileOps:
    """
    Common file functions
    """

    def __init__(self):
        pass

    def _check_file_existance(self, file_path):
        """Check if a file exists. Raise erorr if file not found

        Args:
            file_path (str): file path to check

        Returns:
            None
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError("File does not exist")


class BaseFileIO(BasicFileOps):
    """Base class for file reader
    """

    def __init__(self):
        super().__init__()

    def _read_text_file(
        self, file_path, strip_line=False, delimiter=" ", encoding="utf-8"
    ):
        """Creates a file content generator.

        Args:
            file_path (str): file to read

        Returns:
            generator
        """
        self._check_file_existance(file_path)

        with io.open(file_path, "r", encoding=encoding) as f_in:
            for line in f_in:
                if strip_line:
                    line = line.strip()
                yield line.split(delimiter)

    def _write_to_disk(self, data, file_path, delimiter=" ", encoding="utf-8"):
        """Write data to disk

        Args:
            data (iter): Iterable to write to file
            file_path (str): file to write to

        Returns:
            None
        """
        with io.open(file_path, "w", encoding=encoding) as f_out:
            for line in data:
                f_out.write(delimiter.join(line) + "\n")


class BaseJsonIO(BaseFileIO):
    """
    Base Json file IO functions
    """

    def __init__(self):
        super().__init()

    def read_json(self, file_path, encoding="utf-8"):
        """Reads json file

        Args:
            file_path (str): file to read

        Returns:
            (generator)
        """
        self._check_file_existance(file_path)

        with io.open(file_path, "r", encoding=encoding) as json_in:
            json_contents = json.load(json_in)

        return json_contents

    def write_json(self, data, file_path, encoding="utf-8"):
        """Write dict to disk

        Args:
            data (dict): data to write to disk
            file_path (str): file to dump data
            encoding (str): encoing format for output file

        Returns:
            None
        """
        with io.open(file_path, "w", encoding=encoding) as f_out:
            json.dump(data, f_out, indent=4)


class CsvIO(BaseFileIO):
    """
    Use this to read and process csv files.
    """

    def __init__(self):
        super().__init__()

    def read_csv(self, file_path, strip_line=True):
        """Reads a csv file.

        Args:
            file_path (str): file to read

        Returns:
            (generator)
        """
        return self._read_text_file(
            file_path=file_path, strip_line=strip_line, delimiter=",",
        )

    def write_csv(self, data, file_path):
        """Write csv to disk

        Args:
            data (iterable)
            file_path (str): file to write data to
        """
        self._write_to_disk(data=data, file_path=file_path, delimiter=",")


class TsvIO(BaseFileIO):
    """
    Class to read and process csv files.
    """

    def __init__(self):
        super().__init__()

    def read_tsv(self, file_path, strip_line=True):
        """Reads CSV file.

        Args:
            file_path (str): file to read

        Returns:
            (generator)
        """
        return self._read_text_file(
            file_path=file_path, strip_line=strip_line, delimiter="\t",
        )

    def write_tsv(self, data, file_path):
        """Write TSV file

        Args:
            data (iterable)
            file_path (str): file to write data to
        """
        self._write_to_disk(data=data, file_path=file_path, delimiter="\t")
