import csv
from typing import Dict, List


def read_csv(file_name: str) -> List[Dict[str, object]]:
    with open(file_name, encoding='ISO-8859-1') as file:
        return list(csv.DictReader(file.readlines()))


def get_total_schools(schools: List[Dict[str, object]]) -> int:
    total_schools = len(schools)
    return total_schools


def get_school_counts_by_property(schools: List[Dict[str, object]], *args) -> Dict[str, int]:
    school_counts_by_property = {}
    for school in schools:
        properties = []
        for arg in args:
            properties.append(school[arg])

        property = ", ".join(properties)
        if property not in school_counts_by_property:
            school_counts_by_property[property] = 0

        school_counts_by_property[property] = school_counts_by_property[property] + 1

    return school_counts_by_property


def print_school_counts_by_property(schools: List[Dict[str, object]], property_name: str, header: str) -> None:
    school_counts_by_property = get_school_counts_by_property(
        schools, property_name)
    print(header)
    for property, count in school_counts_by_property.items():
        print(f"   {property}: {count}")


def print_city_with_most_schools(schools: List[Dict[str, object]]) -> None:
    schools_by_city_with_state = get_school_counts_by_property(
        schools, "LCITY05", "LSTATE05")
    city_state_with_most_schools = max(schools_by_city_with_state,
                                             key=schools_by_city_with_state.get)
    city_with_most_schools = city_state_with_most_schools.split(',', 1)[
        0]
    school_count = schools_by_city_with_state[city_state_with_most_schools]
    print(
        f"City with most schools: {city_with_most_schools} ({school_count} schools)")


def print_unique_cities_with_at_least_one_school(schools: List[Dict[str, object]]) -> None:
    schools_by_city_with_state = get_school_counts_by_property(
        schools, "LCITY05", "LSTATE05")
    unique_cities_with_at_least_one_school = len(schools_by_city_with_state)
    print(
        f"Unique cities with at least one school: {unique_cities_with_at_least_one_school}")


def print_counts():
    schools = read_csv("school_data.csv")

    print(f"Total Schools: {get_total_schools(schools)}")
    print()
    print_school_counts_by_property(schools, "LSTATE05", "Schools by State: ")
    print()
    print_school_counts_by_property(
        schools, "MLOCALE", "Schools by Metro-centric locale: ")
    print()
    print_city_with_most_schools(schools)
    print()
    print_unique_cities_with_at_least_one_school(schools)


if __name__ == "__main__":
    print_counts()
