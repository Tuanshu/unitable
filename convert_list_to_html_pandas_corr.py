import pandas as pd


def process_td(current_td, values_list, value_index, non_empty_cell_count, current_row):
    """處理一個單元格的內容，返回更新後的索引和行數據"""
    colspan = 1
    if "colspan" in current_td:
        # 處理含有colspan屬性的單元格
        parts = current_td.split('colspan="')
        colspan = int(parts[1].split('"')[0])
        current_td = parts[0] + 'colspan="' + str(colspan) + '">' + parts[1].split('">')[1]

    if "[]" in current_td and value_index < len(values_list):
        # 處理包含佔位符的單元格
        current_row.extend([values_list[value_index]] * colspan)
        value_index += 1
        non_empty_cell_count += 1
    else:
        # 處理空單元格
        current_row.extend([None] * colspan)

    return current_td, value_index, non_empty_cell_count, current_row


def convert_list_to_html_and_count_cells(table_list, values_list):
    """將列表轉換為HTML並計算非空單元格數量"""
    html_output = []
    html_output.append("<table>")

    non_empty_cell_count = 0
    value_index = 0
    table_data = []
    current_row = []
    current_td = ""
    inside_td = False

    for item in table_list:
        item = item.strip()

        if item == "<thead>" or item == "</thead>" or item == "<tbody>" or item == "</tbody>":
            # 處理表頭和表身的開始和結束標籤
            html_output.append(item)
            if current_row:
                table_data.append(current_row)
            current_row = []
        elif item.startswith("<tr>"):
            # 處理行的開始標籤
            if current_row:
                table_data.append(current_row)
            current_row = []
            html_output.append(item)
        elif item.startswith("</tr>"):
            # 處理行的結束標籤
            html_output.append(item)
            if current_row:
                table_data.append(current_row)
            current_row = []
        elif item.endswith("</td>"):
            # 處理單元格的結束標籤
            current_td += item
            inside_td = False
            current_td, value_index, non_empty_cell_count, current_row = process_td(
                current_td, values_list, value_index, non_empty_cell_count, current_row
            )
            html_output.append(current_td)
            current_td = ""
        elif item.startswith("<td"):
            # 處理單元格的開始標籤
            current_td = item
            inside_td = True
        elif inside_td:
            # 處理單元格內的其他標籤或內容
            current_td += item
        else:
            # 處理其他標籤或內容
            html_output[-1] = html_output[-1].replace(">", f">{item}")
            if "[]" in item and value_index < len(values_list):
                current_row[-1] = values_list[value_index]
                value_index += 1
                non_empty_cell_count += 1

    if current_row:
        table_data.append(current_row)

    html_output.append("</table>")

    return "\n".join(html_output), non_empty_cell_count, table_data


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


html_result, non_empty_cell_count, table_data = convert_list_to_html_and_count_cells(table_list, values_list)
print(html_result)
print(f"Non-empty cell count: {non_empty_cell_count}")

# Convert table_data to a pandas DataFrame
df = pd.DataFrame(table_data)

# # Display the DataFrame
# import ace_tools as tools

# tools.display_dataframe_to_user(name="HTML Table Data", dataframe=df)

print(df)
