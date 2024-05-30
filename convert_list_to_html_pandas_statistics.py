import pandas as pd


class HTMLTableStatistics:
    def __init__(self, table_list, values_list):
        self.table_list = table_list
        self.values_list = values_list
        self.html_output = ""
        self.non_empty_cell_count = 0
        self.table_data = []
        self.value_index = 0
        self.max_columns = 0
        self.num_rows = 0
        self.num_rows_no_span_from_bottom = 0
        self.num_rows_with_span_from_top = 0

        self._convert_list_to_html_and_calculate_statistics()

    def _process_td(self, current_td, current_row):
        """處理一個單元格的內容，返回更新後的索引和行數據"""
        colspan = 1
        if "colspan" in current_td:
            parts = current_td.split('colspan="')
            colspan = int(parts[1].split('"')[0])
            current_td = parts[0] + 'colspan="' + str(colspan) + '">' + parts[1].split('">')[1]

        if "[]" in current_td and self.value_index < len(self.values_list):
            current_row.extend([self.values_list[self.value_index]] * colspan)
            self.value_index += 1
            self.non_empty_cell_count += 1
        else:
            current_row.extend([None] * colspan)

        return current_td, current_row

    def _convert_list_to_html_and_calculate_statistics(self):
        """將列表轉換為HTML並計算統計數據"""
        html_output = []
        html_output.append("<table>")

        current_row = []
        current_td = ""
        inside_td = False

        for item in self.table_list:
            item = item.strip()

            if item == "<thead>" or item == "</thead>" or item == "<tbody>" or item == "</tbody>":
                html_output.append(item)
                if current_row:
                    self.table_data.append(current_row)
                current_row = []
            elif item.startswith("<tr>"):
                if current_row:
                    self.table_data.append(current_row)
                current_row = []
                html_output.append(item)
            elif item.startswith("</tr>"):
                html_output.append(item)
                if current_row:
                    self.table_data.append(current_row)
                current_row = []
            elif item.endswith("</td>"):
                current_td += item
                inside_td = False
                current_td, current_row = self._process_td(current_td, current_row)
                html_output.append(current_td)
                current_td = ""
            elif item.startswith("<td"):
                current_td = item
                inside_td = True
            elif inside_td:
                current_td += item
            else:
                html_output[-1] = html_output[-1].replace(">", f">{item}")
                if "[]" in item and self.value_index < len(self.values_list):
                    current_row[-1] = self.values_list[self.value_index]
                    self.value_index += 1
                    self.non_empty_cell_count += 1

        if current_row:
            self.table_data.append(current_row)

        html_output.append("</table>")
        self.html_output = "\n".join(html_output)

        # 計算統計數據
        self.num_rows = len(self.table_data)
        self.max_columns = max(len(row) for row in self.table_data)

        # 計算從下方開始沒有span的行數
        for row in reversed(self.table_data):
            if len(row) == self.max_columns:
                self.num_rows_no_span_from_bottom += 1
            else:
                break

        # 計算從上方開始有span的行數
        for row in self.table_data:
            span_detected = False
            col_count = 0
            for cell in row:
                if cell is not None:
                    col_count += 1
                else:
                    span_detected = True
                    break
            if span_detected or col_count < self.max_columns:
                self.num_rows_with_span_from_top += 1
            else:
                break

    def get_statistics(self):
        """返回統計數據"""
        return {
            "number_of_rows": self.num_rows,
            "max_number_of_columns": self.max_columns,
            "number_of_rows_no_span_from_bottom": self.num_rows_no_span_from_bottom,
            "number_of_rows_with_span_from_top": self.num_rows_with_span_from_top,
        }


table_list = [
    "<thead>",
    "<tr>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td",
    "  ",
    'colspan="2"',
    ">[]</td>",
    "<td",
    "  ",
    'colspan="3"',
    ">[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td></td>",
    "<td></td>",
    "<td></td>",
    "<td",
    "  ",
    'colspan="2"',
    ">[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "</tr>",
    "</thead>",
    "<tbody>",
    "<tr>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "<td></td>",
    "<td>[]</td>",
    "</tr>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td></td>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "</tbody>",
]
values_list = [
    "Main cellular process",
    "Modulated pathways",
    "P value",
    "Genes in pathway",
    "Expressed",
    "total",
    "+ PMN",
    "- PMN",
    "+ PMN",
    "PMN",
    "Cell cycle",
    "Role of APC in cell cycle regulation",
    "1.040E - 09",
    "8.149E - 08",
    "15",
    "12",
    "32",
    "Chromosome condensation in prometaphase",
    "4.131E - 06",
    "8.392E - 11",
    "9",
    "12",
    "20",
    "The metaphase checkpoint",
    "4.423E - 06",
    "1.474E - 04",
    "12",
    "9",
    "36",
    "Spindle assembly and chromosome separation",
    "3.170E - 04",
    "1.937E - 03",
    "9",
    "7",
    "32",
    "Start of DNA replication in early S phase",
    "1.284E - 03",
    "3.115E - 02",
    "8",
    "5",
    "31",
    "Initiation of mitosis",
    "1.544E - 03",
    "2.483E - 03",
    "7",
    "6",
    "25",
    "Sister chromatid cohesion",
    "1.530E - 02",
    "5",
    "21",
    "Transition and termination of DNA replication",
    "1.523E - 02",
    "5",
    "26",
    "Role of Nek in cell cycle regulation",
    "2.390E - 02",
    "5",
    "29",
    "Nucleocytoplasmic transport of CDK / Cyclins",
    "4.386E - 02",
    "3",
    "14",
    "Immune response",
    "Alternative complement pathway",
    "4.539E - 07",
    "2.737E - 02",
    "12",
    "5",
    "30",
    "Fc gamma R - mediated phagocytosis",
    "1.606E - 03",
    "9.058E - 03",
    "8",
    "6",
    "32",
    "Antigen presentation by MHC class II",
    "6.046E - 03",
    "2.644E - 03",
    "4",
    "4",
    "11",
    "Classic complement pathway",
    "1.517E - 05",
    "12",
    "40",
    "Antiviral actions of Interferons",
    "2.431E - 04",
    "9",
    "31",
    "CCR3 signalling",
    "8.728E - 04",
    "12",
    "59",
    "Lectin Induced complement pathway",
    "1.251E - 03",
    "9",
    "38",
    "Lipoxin inhibitory action on Superoxide production",
    "1.544E - 03",
    "2.483E - 03",
    "7",
    "6",
    "25",
    "IFN alpha / beta signalling pathway",
    "6.214E - 03",
    "6",
    "24",
    "IL - 10 signalling pathway",
    "2.245E - 02",
    "5",
    "23",
    "Antigen presentation by MHC class I",
    "3.675E - 02",
    "5",
    "26",
    "Transcription regulation of granulocyte development",
    "3.115E - 02",
    "5",
    "31",
    "Oxidative stress",
    "ROS production",
    "8.932E - 04",
    "4.113E - 02",
    "7",
    "4",
    "23",
    "Apoptosis",
    "Inhibition of ROS induced apoptosis",
    "3.675E - 02",
    "5",
    "26",
    "G protein signalling",
    "Rac2 regulation pathway",
    "4.957E - 03",
    "4.113E - 02",
    "6",
    "4",
    "23",
    "RAC1 in cellular process",
    "1.361E - 02",
    "6",
    "28",
    "Cytoskeleton remodelling",
    "Regulation of actin cytoskeleton by Rho GTPases",
    "8.972E - 03",
    "5",
    "23",
    "Alpha - 1A adrenergic receptor - dependent inhibition of PI3K",
    "2.887E - 02",
    "3",
    "12",
    "Metabolic process",
    "Lipoprotein metabolism I. Chylomicron, VLDL and LDL metabolism",
    "1.630E - 02",
    "9.007E - 07",
    "3",
    "6",
    "8",
    "Lipoprotein metabolism II. HDL metabolism",
    "1.630E - 02",
    "9.007E - 07",
    "3",
    "6",
    "8",
    "G - alpha ( q ) regulation of lipid metabolism",
    "2.245E - 02",
    "5",
    "23",
    "Urea cycle",
    "3.675E - 02",
    "5",
    "26",
    "LDL metabolism during development of fatty streak lesion",
    "1.870E - 02",
    "2",
    "4",
]


stats = HTMLTableStatistics(table_list, values_list)
html_result = stats.html_output
statistics = stats.get_statistics()

print(html_result)
print(statistics)

# 將table_data轉換為Pandas DataFrame
df = pd.DataFrame(stats.table_data)
print(df)
