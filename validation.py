from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
import matplotlib.pyplot as plt


#validating the data is there in present db or not
def compare_domains(domain_list, db_domains):
    print(domain_list)
    print(db_domains)
    matched_domains = []
    unmatched_domains = []
    try:

        for domain in domain_list:
            domain_lower = domain.lower()
            print(domain_lower)

            if any(domain_lower in db_domain.lower() or
                fuzz.partial_ratio(domain_lower, db_domain.lower()) >= 85 or
                fuzz.token_sort_ratio(domain_lower, db_domain.lower()) >= 85
                for db_domain in db_domains):
                matched_domains.append(domain)
            else:
                unmatched_domains.append(domain)
    except Exception as ex:
        print(ex)
            
    return matched_domains, unmatched_domains