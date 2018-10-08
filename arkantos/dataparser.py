import csv


class DataParser:

    @classmethod
    def read_csv_as_list(cls, filename: str) -> list:
        """
        read csv file content and return list

        :param str filename: file name

        :rtype: list
        :return: csv file content
        """
        return [row for row in csv.DictReader(open(filename))]
