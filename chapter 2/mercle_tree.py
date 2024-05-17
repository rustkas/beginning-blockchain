from hashlib import sha256

class MerkelTree(object):
    def __init__(self):
        pass 

    def chunks(self, transactions, n):
        # This function yields "n" number of transactions at a time
        for i in range(0, len(transactions), n):
            yield transactions[i:i + n]

    def merkel_tree(self, transactions):
        # Here we will find the merkel tree hash of all transactions passed to this function
        # Problem is solved using recursion technique
        # Given a list of transactions, we concatenate the hashes in groups of two and compute
        # the hash of the group, then keep the hash of the group. We repeat this step till
        # we reach a single hash
        sub_tree = []
        for chunk in self.chunks(transactions, 2):
            if len(chunk) == 2:
                hash = sha256((chunk[0] + chunk[1]).encode('utf-8')).hexdigest()
            else:
                hash = sha256((chunk[0] + chunk[0]).encode('utf-8')).hexdigest()
            sub_tree.append(hash)
        # When the sub_tree has only one hash then we reached our merkel tree hash.
        # Otherwise, we call this function recursively
        if len(sub_tree) == 1:
            return sub_tree[0]
        else:
            return self.merkel_tree(sub_tree)

if __name__ == '__main__':
    mk = MerkelTree()
    merkel_hash = mk.merkel_tree(["TX1", "TX2", "TX3", "TX4", "TX5", "TX6"])
    print(merkel_hash)
