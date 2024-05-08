from scenarios.show import show_scenario
from scenarios.create import create_scenario
from scenarios.edit import edit_scenario
from scenarios.search import search_scenario

scenarios_dict = {
    1: show_scenario,
    2: create_scenario,
    3: edit_scenario,
    4: search_scenario,
}
