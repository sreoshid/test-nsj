def getclientCodeFromUser():
      clientCode = ""
      while True:
        clientCode = raw_input("Enter the Location/Client Code: ")
        if (clientCode in ['RDU', 'LGA', 'EWR', 'JFK', 'ZRH', 'LHR', 'PHX']):
            break
      return clientCode

print (getclientCodeFromUser())