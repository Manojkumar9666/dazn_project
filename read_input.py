import pandas as pd


# Function to read keywords from Excel file
def read_keywords_from_excel(file_path):
    df = pd.read_excel(file_path, sheet_name='keywords')  # Update sheet name if necessary
    keywords = df['Keyword'].tolist()  # Assuming 'Keyword' is the column name
    print(keywords)
    return keywords