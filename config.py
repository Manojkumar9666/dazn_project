import pandas as pd


def get_paths():
    df = pd.read_excel(r"config\\configuration_file.xlsx", sheet_name='path_details')
    return df["input_excel_path"][0], df["output_excelpath"][0] , df["driver_path"][0]