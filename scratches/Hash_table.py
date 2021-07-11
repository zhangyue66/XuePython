class HashTable():
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        hv = self.calculate_hash_value(string)
        if hv != -1:
           if self.table[hv] != None:
              self.table[hv].append(string)
           else:
               self.table[hv] =[string]


    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if self.table[hv] !=None:
           if string in self.table[hv]:
              return hv
        else:
            return -1

    def calculate_hash_value(self, string):
        b = list(string)
        hash_value = ord(b[0])*100+ord(b[1])
        return hash_value

hash_table = HashTable()

print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
#print(hash_table.table)
print( hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')

# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
#print(hash_table.table)
# Should be 8568
print (hash_table.lookup('UDACIOUS'))
#

