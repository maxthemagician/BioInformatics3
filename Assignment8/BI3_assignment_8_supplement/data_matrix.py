import re
from scipy import stats

class DataMatrix:
    def __init__(self, file_path):
        """
        :param file_path: path to the input matrix file
        """
        self.file_path = file_path
        # TODO: define and initialise the class fields you need for your implementation
        # read the matrix in the input file, remove rows with empty values and merge duplicate rows
        self.dict_row = {}
        self.dict_col = {}
        self.read_data()


    def read_data(self):
        """
        Reads data from a given matrix file, where the first line gives the names of the columns and the first column
        gives the names of the rows. Removes rows with empty or non-numerical values and merges rows with the same
        name into one.
        """
        file = open(self.file_path, "r")
        for i, line in enumerate(file):
            line = line.strip('\n')
            temp = re.split(r'\t+', line)  # split line after tab

            if i == 0:
                colnames = temp[1:len(temp)]
                for j in range(len(colnames)):
                    self.dict_col[colnames[j]] = []
            if i > 0:
                if all(str(x).strip('-').replace('.', '').isdigit() and x != '' for x in temp[1:len(temp)]):
                    row = map(float, temp[1:len(temp)])
                    if temp[0] in self.dict_row.keys():
                        self.dict_row[temp[0]] = [((x + y) / 2) for x, y in zip(self.dict_row[temp[0]], row)]
                    else:
                        self.dict_row[temp[0]] = row
                    for j in range(len(colnames)):
                        self.dict_col[colnames[j]].append(self.dict_row[temp[0]][j])

    def get_rows(self):
        """
        :return: dictionary with keys = row names, values = list of row values
        """
        return self.dict_row

    def get_columns(self):
        """
        :return: dictionary with keys = column names, values = list of column values
        """
        self.dict_col

    def not_normal_distributed(self, alpha, rows):
        """
        Uses the Shapiro-Wilk test to compute all rows (or columns) that are not normally distributed.
        :param alpha: significance threshold
        :param rows: True if the Shapiro-Wilk p-values should be computed for the rows, False if for the columns
        :return: dictionary with keys = row/columns names, values = Shapiro-Wilk p-value
        """
        if(rows):   dict = self.dict_row
        else:   dict = self.dict_col
        dict_p_shapiro = {}

        for key in dict.keys():
            shapiro = stats.shapiro(dict[key])
            if shapiro[1] < alpha:
                dict_p_shapiro[key] = shapiro[1]

        return dict_p_shapiro

    def to_tsv(self, file_path):
        """
        Writes the processed matrix into a tab-separated file, with the same column order as the input matrix and
        the rows in lexicographical order.
        :param file_path: path to the output file
        """
        dict_row_sorted = sorted(self.dict_row)
        file = open(file_path, 'w')
        list_of_lines = [' ' + '\t'.join(self.dict_col.keys())]
        for i in range(len(self.dict_row)):
            line = dict_row_sorted[i] + '\t' + ('\t'.join([str(x) for x in self.dict_row[dict_row_sorted[i]]]))
            list_of_lines.append(line)
        file.write("\n".join(list_of_lines))
