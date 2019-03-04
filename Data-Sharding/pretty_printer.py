import pprint


def prettyPrint(dict_to_print):
    pp = pprint.PrettyPrinter(indent=4, width=1000)
    pp.pprint(dict_to_print)