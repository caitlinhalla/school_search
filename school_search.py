import csv
from typing import Dict, List, Tuple
import time
import itertools


def read_csv(file_name: str) -> List[Dict[str, object]]:
    with open(file_name, encoding='ISO-8859-1') as file:
        schools_data = list(csv.DictReader(file.readlines()))
        columns_to_remove = ('NCESSCH', 'LEAID', 'LEANM05', 'LATCOD',
                             'LONCOD', 'MLOCALE', 'ULOCALE', 'status05')
        for row in schools_data:
            for column_name in columns_to_remove:
                row.pop(column_name, None)
        return schools_data


schools_data = read_csv("school_data.csv")


def count_matches(list_a: List[str], list_b: List[str]) -> int:
    count = 0

    for item_a in list_a:
        for item_b in list_b:
            if item_a == item_b:
                count += 1
    return count


def find_school_matches(query: str) -> Tuple[int, str, str, str]:
    normalized_query = " ".join(query.split()).upper()
    query_list = list(normalized_query.split(" "))

    school_match_results_with_count = []
    school_match_results = []
    for school in schools_data:
        school_values_list = list(itertools.chain.from_iterable(
            [school_value.split() for school_value in school.values()]))
        normalized_school_values = " ".join(school_values_list)
        school_match_count = count_matches(
            query_list, school_values_list)

        if normalized_query in normalized_school_values:
            school_match_results_with_count.append((school, 100))
        elif school_match_count > 0:
            school_match_results_with_count.append(
                (school, school_match_count))

    ordered_list_counter = 1
    sorted_school_matches = sorted(
        school_match_results_with_count, key=lambda result: result[1], reverse=True)[:3]
    for school, school_match_count in sorted_school_matches:
        school_match_results.append((ordered_list_counter, school['SCHNAM05'],
                                     school['LCITY05'], school['LSTATE05']))
        ordered_list_counter += 1

    return school_match_results


def search_schools(query: str) -> None:
    start_time = time.time()
    school_matches = find_school_matches(query)

    print(
        f"Results for \"{query}\" (search took: {(time.time() - start_time)}s)")
    [print(
        f"{counter}. {school_name} \n   {city}, {state}") for counter, school_name, city, state in school_matches]


if __name__ == "__main__":
    search_schools("elementary school highland park")
    search_schools("jefferson belleville")
    search_schools("riverside school 44")
    search_schools("granada charter school")
    search_schools("foley high alabama")
    search_schools("KUSKOKWIM")
