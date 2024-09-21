import os
import pandas as pd
import logging

def save_results_to_excel(results, output_path):
    if not os.path.isfile(output_path):
        logging.info(f"Excel file '{output_path}' not found. Creating new file.")
        mode = 'w'  # Create new file if it doesn't exist
    else:
        mode = 'a'  # Append to existing file
    
    with pd.ExcelWriter(output_path, engine='openpyxl', mode=mode) as writer:
        for keyword, domains in results.items():
            domain_df = pd.DataFrame(domains["all_domains"], columns=["Domain"])
            try:
                domain_df.to_excel(writer, sheet_name=keyword, index=False)
                logging.info(f"Data for '{keyword}' appended to Excel sheet successfully.")
            except Exception as e:
                logging.error(f"Error writing to Excel: {e}")
