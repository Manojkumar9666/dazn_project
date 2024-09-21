import logging, os
import pandas as pd
from save_excel import save_results_to_excel
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from extract_infringing_logic import get_infringing_links
import requests
from visulization import create_dashboard, create_wordcloud
import time
from urllib.parse import urlparse, parse_qs
from validation import compare_domains
from read_input import read_keywords_from_excel
from database import fetch_data, insert_matched_domain, insert_unmatched_domain, setup_database, create_table
from init_driver import setup_driver
from config import get_paths

# Create 'process_logs' directory if it doesn't exist
log_directory = 'process_logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging to write to both console and file
log_file = os.path.join(log_directory, 'process.log')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Get file paths from configuration
    excel_file_path = get_paths()[0]
    output_excel_path = get_paths()[1]

    try:
        # Read keywords from Excel file
        keywords = read_keywords_from_excel(excel_file_path)
    except Exception as e:
        logging.error(f"Error reading Excel file: {e}")
        return

    results = {}

    # Iterate over each keyword and process
    for keyword in keywords:
        start_time = time.time()  # Start recording time for the keyword processing
        try:
            # Initialize the Selenium driver
            driver = setup_driver()
            
            # Get infringing links from Google search
            infringing_links = get_infringing_links(driver, keyword)
            
            # Fetch domains from database
            db_domains = fetch_data()
            
            # Compare infringing links with database domains
            matched_domains, unmatched_domains = compare_domains(infringing_links, db_domains)

            # Log matched and unmatched domains
            logging.info(f"Matched domains found for '{keyword}': {matched_domains}")
            logging.info(f"Unmatched domains found for '{keyword}': {unmatched_domains}")

            # Insert matched domains into the database
            for domain in matched_domains:
                try:
                    insert_matched_domain(domain)
                except Exception as e:
                    logging.error(f"Error inserting matched domain '{domain}': {e}")

            # Insert unmatched domains into the database
            for domain in unmatched_domains:
                try:
                    insert_unmatched_domain(domain)
                except Exception as e:
                    logging.error(f"Error inserting unmatched domain '{domain}': {e}")

            # Store results for the keyword
            results[keyword] = {
                "matched_domains": matched_domains,
                "unmatched_domains": unmatched_domains,
                "all_domains": matched_domains + unmatched_domains,
                "process_time": time.time() - start_time  # Record total process time
            }
        except Exception as e:
            logging.error(f"Error processing keyword '{keyword}': {e}")
        finally:
            driver.quit()  # Quit the Selenium driver after processing

    try:
        # Save results to Excel file
        save_results_to_excel(results, output_excel_path)
    except Exception as e:
        logging.error(f"Error saving results to Excel: {e}")

    # Create and display dashboard with visualization
    create_dashboard(results)


if __name__ == "__main__":
    setup_database()  # Initialize the database setup
    main()  # Execute the main function to process keywords and visualize results
