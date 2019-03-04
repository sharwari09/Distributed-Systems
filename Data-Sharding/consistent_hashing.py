import csv_parser
import requests
import sys
from logger import *
import pretty_printer

servers = ['http://localhost:5000', 'http://localhost:5001',
           'http://localhost:5002', 'http://localhost:5003']


class ConsistentHashing:
    def __init__(self, no_of_servers, input_file):
        self.no_of_servers = no_of_servers
        server_compute = [(j, hash(servers[j])) for j in
                          range(self.no_of_servers)]
        server_compute.sort(
            key=lambda hash_key: hash_key[1]
        )
        self.server_compute = server_compute
        self.input_file = input_file

    def mapServer(self, key_hash):
        if key_hash > self.server_compute[-1][1]:
            return 0
        for entry in self.server_compute:
            if entry[1] > key_hash :
                break
        return entry[0]

    def postToDataStore(self):
        cnt = 0
        for entry in csv_parser.parse_csv(self.input_file):
            cnt += 1
            key = str(entry[0] + entry[2] + entry[3])
            key_hash = hash(key)
            machine_id = self.mapServer(key_hash)
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

        log(LOG_LEVEL=LOG_INFO, logmsg="\n\nConsistent Hashing Key"
                                        " Distribution:\n")
        pretty_printer.prettyPrint(num_entry_list)

    def printServerCompute(self):
        for (j, h) in self.server_compute:
            print("Server: %s\tServer Hash: %s" % (j, h))


def main():
    sh = ConsistentHashing(len(servers), sys.argv[1])
    sh.printServerCompute()
    sh.postToDataStore()
    sh.getFromDatastore()



if __name__ == "__main__":
    main()
