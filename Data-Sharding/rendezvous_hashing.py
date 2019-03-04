import csv_parser
import requests
import sys
from logger import *
import pretty_printer

servers = ['http://localhost:5000', 'http://localhost:5001',
           'http://localhost:5002', 'http://localhost:5003']


class RendezvousHashing:
    def __init__(self, no_of_servers, input_file):
        self.no_of_servers = no_of_servers
        self.server_compute = [j for j in range(self.no_of_servers)]
        self.input_file = input_file

    def mapServer(self, key):
        server_score, server = None, None
        for node in self.server_compute:
            score = hash(key + str(node))
            if server_score is None or score > server_score:
                server, server_score = node, score
        return server

    def postToDataStore(self):
        cnt = 0
        for entry in csv_parser.parse_csv(self.input_file):
            cnt += 1
            key = str(entry[0] + entry[2] + entry[3])
            key_hash = hash(key)
            machine_id = self.mapServer(key)
            requests.post("{}/api/v1/entries".format(servers[machine_id]),
                          json={key_hash: ",".join(entry)})
        log(LOG_LEVEL=LOG_INFO, logmsg="Uploaded all {} entries.".format(cnt))

    def getFromDatastore(self):
        num_entry_list = []
        log(LOG_LEVEL=LOG_INFO, logmsg="Verifying the data.")
        for server in servers:
            response = requests.get("{}/api/v1/entries".format(server))
            num_entry_list.append({"num_entries": response.json()['num_entries']})
            log(LOG_LEVEL=LOG_INFO,
                logmsg="GET {}".format(server)
                )
            pretty_printer.prettyPrint(response.json())
        log(LOG_LEVEL=LOG_INFO, logmsg="\n\nRendezvous Hashing Key"
                                        " Distribution:\n")
        pretty_printer.prettyPrint(num_entry_list)

    def printServerCompute(self):
        for (j) in self.server_compute:
            print("Server: (%s)" % (j))


def main():
    sh = RendezvousHashing(len(servers), sys.argv[1])
    sh.printServerCompute()
    sh.postToDataStore()
    sh.getFromDatastore()


if __name__ == "__main__":
    main()
