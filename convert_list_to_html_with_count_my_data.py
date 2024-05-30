def convert_list_to_html_and_count_cells(table_list):
    html_output = []
    html_output.append("<table>")

    in_thead = False
    in_tbody = False
    non_empty_cell_count = 0

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
        elif item.startswith("<tr>") or item.startswith("</tr>"):
            html_output.append(item)
        elif item.startswith("<td") or item.startswith("</td>"):
            html_output.append(item)
            if "[]" in item:
                non_empty_cell_count += 1
        else:
            html_output[-1] = html_output[-1].replace(">", f">{item}")
            if "[]" in item:
                non_empty_cell_count += 1

    html_output.append("</table>")

    return "\n".join(html_output), non_empty_cell_count


table_list = [
    "<thead>",
    "<tr>",
    "<td></td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
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
    "</tr>",
    "<tr>",
    "<td></td>",
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
    "</tr>",
    "<tr>",
    "<td></td>",
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
    "</tr>",
    "<tr>",
    "<td></td>",
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
    "</tr>",
    "<tr>",
    "<td></td>",
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
    "</tr>",
    "<tr>",
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
    "</tr>",
    "<tr>",
    "<td></td>",
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
    "</tr>",
    "<tr>",
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
    "</tr>",
    "<tr>",
    "<td></td>",
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
    "</tr>",
    "<tr>",
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
    "<td>[]</td>",
    "<td>[]</td>",
    "<td>[]</td>",
    "</tr>",
    "</tbody>",
]


html_result, non_empty_cell_count = convert_list_to_html_and_count_cells(table_list)
print(html_result)
print(f"Non-empty cell count: {non_empty_cell_count}")
