import oyez_api_wrapper
import json

YEAR_RANGE = [2000, 2001]

assert YEAR_RANGE[0] <= YEAR_RANGE[1]
assert 1776 <= YEAR_RANGE[0]
assert YEAR_RANGE[1] <= 2024

years = []
curr_year = YEAR_RANGE[0]
while curr_year <= YEAR_RANGE[1]:
    years.append(curr_year)
    curr_year += 1
print("YEARS TO BE SCRAPED: ", years)

# case_obj = oyez_api_wrapper.court_case("2015", "15-278")
# print(case_obj.get_case_judges())    

# now pull all the data

for year in years:
    case_numbers = ["00-24", "01-46"]
    # case_numbers = generate_supreme_court_case_numbers(year, MAX_CASE_NUMBER)
    for case_number in case_numbers:
        try:
            print("YEAR: {} CASE NUMBER: {}".format(year, case_number))
            case_obj = oyez_api_wrapper.court_case(year, case_number)
            print(case_obj.get_ruling())
        except:
            print("FAILURE")
        else:
            print("SUCCESS")
            print(case_obj.get_case_judges())
            print(case_obj.get_case_facts())
            print(case_obj.get_judge_decisions())
            print(case_obj.get_ruling())
            print(case_obj.get_basic_info())
            print(case_obj.get_legal_question())
            print(case_obj.get_conclusion())
            print(case_obj.get_lower_court())




