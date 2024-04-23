# scotus-predictor/oyez_scraper.py
# author: rajamoreno

# import oyez_api_wrapper
import requests
import json
import csv
import re
from six import string_types

# Important note:

# This script relies on first downloading a file called cases.json, accessible via Oyez's unlisted API at:
#   http://api.oyez.org/cases?per_page=0
# Feel free to substitute an updated version of that file for the one included in this repo.

# With gratitude to:

# tylzars, the author of oyez_api_wrapper:
#   https://github.com/tylzars/oyez-api-wrapper
# Some of the error handling in oyez_api_wrapper wasn't quite tuned the way I wanted, 
# so I copied and modified tylzars's code for this project. 
# The structure of court_case is similar but streamlined for just the functionality I need.

# walkerdb, for describing his experimentation with the Oyez API here:
#   https://github.com/walkerdb/supreme_court_transcripts/issues/1#issuecomment-377104119

# Real Python, for their tutorial on using json data in Python:
#   https://realpython.com/python-json/

class court_case:

    def __init__(self, term, docket_number):

        if not term and not docket_number:
            # raise ValueError("term and docket_number are both mandatory.")
            return None

        if (term and not isinstance(term, string_types)) and (docket_number and not isinstance(docket_number, string_types)):
            # raise TypeError("term and docket_number must both be strings.")
            return None

        self.term = term
        self.docket_number = docket_number
        
        try:
            response = requests.get(f"https://api.oyez.org/cases/{self.term}/{self.docket_number}")
            response.raise_for_status()  # This will raise an HTTPError for bad responses
            self.json_data = response.json()
        except requests.exceptions.HTTPError as http_err:
            print("HTTP ERROR: ", http_err)
            self.json_data = None
        except json.JSONDecodeError as json_err:
            print("JSON ERROR: ", json_err)
            self.json_data = None
        except Exception as e:
            print("OTHER ERROR: ", e)
            self.json_data = None

    def get_case_justices(self):

        decisions = self.json_data.get("decisions", {})
        
        if isinstance(decisions, list) and len(decisions) > 0 and isinstance(decisions[0], dict):
            votes = decisions[0].get("votes", {})
            if votes:
                justice_names = []
                for vote in votes:
                    justice_name = vote.get("member", {}).get("name", {})
                    justice_names.append(justice_name)
                return justice_names
            else:
                return None
        else:
            return None
        
    def get_case_facts(self):
        facts = self.json_data.get("facts_of_the_case", {})
        if isinstance(facts, str) and facts != "":
            return re.sub('<[^<]+?>', '', facts)
        else:
            return None
    
    def get_case_question(self):
        question = self.json_data.get("question", {})
        if isinstance(question, str) and question != "":
            return re.sub('<[^<]+?>', '', question)
        else:
            return None
    
    def get_case_conclusion(self):
        conclusion = self.json_data.get("conclusion", {})
        if isinstance(conclusion, str) and conclusion != "":
            return re.sub('<[^<]+?>', '', conclusion)
        else:
            return None
        
with open("cases.json", "r") as read_file:

    data = json.load(read_file)
    number_of_cases = len(data)
    print("NUMBER OF TOTAL CASES: ", number_of_cases)

with open("case_justices_facts_question_conclusion.csv", "w", newline="") as write_file:

    csv_writer = csv.writer(write_file)
    csv_writer.writerow(["Case Key", "Justices", "Facts", "Question", "Conclusion"])

    for i in range(number_of_cases):
    # for i in range(20): # enough to see sample behavior

        href_api = data[i]['href']
        # print(href_api)
        # href_reg = href_api.replace('api.', '') # to get GUI version of Oyez page
        href_api_split = href_api.split("/")
        # print(href_split)
        year = href_api_split[-2]
        case_number = href_api_split[-1]
        key = year + "/" + case_number

        print("Considering case {} of {}: {}".format(i + 1, number_of_cases, key))

        current_case = court_case(year, case_number)
        if current_case.json_data is None:
            continue # this handles the case where the http request failed
        case_justices = current_case.get_case_justices()
        if case_justices:
            case_justices_joined = ', '.join(current_case.get_case_justices())
        # print(case_justices)
        case_facts = current_case.get_case_facts()
        # print(case_facts)
        case_question = current_case.get_case_question()
        # print(case_question)
        case_conclusion = current_case.get_case_conclusion()
        # print(case_conclusion)

        if case_justices and case_facts and case_question and case_conclusion:
            csv_writer.writerow([key, case_justices_joined, case_facts, case_question, case_conclusion])
            print("{} ADDED TO FILE".format(key))





