class Table:
    def __init__(self):
        self.table = []

    def insert(self, item):
        # get the bucket
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item at end of bucket
        bucket_list.append(item)

    def insert(self, key, item):
        # get the bucket where item goes
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # if already in bucket, update
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if not found, add to end of list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        # get the bucket where item goes
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        print(bucket_list)

        # search for key in bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        # get the bucket where item goes
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # if found, remove
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    def printTable(self):
        for i in range(len(self.table) + 1):
            print('print table here')
