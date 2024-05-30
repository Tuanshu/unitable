import pandas as pd


def convert_list_to_html_and_count_cells(table_list, values_list):
    html_output = []
    html_output.append("<table>")

    in_thead = False
    in_tbody = False
    non_empty_cell_count = 0
    value_index = 0
    table_data = []
    current_row = []

    for item in table_list:
        item = item.strip()

        if item == "<thead>":
            html_output.append("<thead>")
            in_thead = True
        elif item == "</thead>":
            html_output.append("</thead>")
            in_thead = False
        elif item == "<tbody>":
            html_output.append("<tbody>")
            in_tbody = True
        elif item == "</tbody>":
            html_output.append("</tbody>")
            in_tbody = False
        elif item.startswith("<tr>"):
            if current_row:
                table_data.append(current_row)
            current_row = []
            html_output.append(item)
        elif item.startswith("</tr>"):
            html_output.append(item)
            if current_row:
                table_data.append(current_row)
            current_row = []
        elif item.startswith("<td"):
            if "colspan" in item:
                html_output.append(item)
            else:
                html_output.append(item)
                if "[]" in item and value_index < len(values_list):
                    current_row.append(values_list[value_index])
                    value_index += 1
                else:
                    current_row.append(None)
        else:
            html_output[-1] = html_output[-1].replace(">", f">{item}")
            if "[]" in item and value_index < len(values_list):
                current_row[-1] = values_list[value_index]
                value_index += 1

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