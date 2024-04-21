# scotus-predictor/oyez_scraper.py
# author: rajamoreno

import oyez_api_wrapper
import json

# This script relies on first downloading a file called cases.json, accessible via Oyez's unlisted API at:
#   http://api.oyez.org/cases?per_page=0
# A current version

# With gratitude to:
# tylzars, the author of oyez_api_wrapper, which made processing Oyez's data much easier
#   https://github.com/tylzars/oyez-api-wrapper
# walkerdb, for describing his experimentation with the Oyez API here:
#   https://github.com/walkerdb/supreme_court_transcripts/issues/1#issuecomment-377104119
# Real Python, for their tutorial on using json data in Python:
#   https://realpython.com/python-json/

with open("cases.json", "r") as read_file:
    data = json.load(read_file)
    print("NUMBER OF ENTRIES: ", len(data))
    for i in range(3):
        href = data[i]['href']
        # print(href)
        href_split = href.split("/")
        # print(href_split)
        year = href_split[-2]
        case_number = href_split[-1]
        print(year, case_number)

        # This data collection uses oyez_api_wrapper, but handling of NoneType is inconsistent,
        # so instead I'm rewriting this for myself.
        case_obj = oyez_api_wrapper.court_case(year, case_number)
        case_basic_info = case_obj.get_basic_info()
        print(case_basic_info)
        case_judges = case_obj.get_case_judges()
        print(case_judges)
        case_facts = case_obj.get_case_facts()
        print(case_facts)
        case_legal_question = case_obj.get_legal_question()
        print(case_legal_question)
        case_ruling = case_obj.get_ruling()
        print(case_ruling)
        case_conclusion = case_obj.get_conclusion()
        print(case_conclusion)
        print(case_obj.get_judge_decisions())
        case_lower_court = case_obj.get_lower_court()
        print(case_lower_court)




