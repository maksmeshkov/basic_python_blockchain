from MinimalBlock import MinimalBlock
import time


class MinimalChain:
    def __init__(self):  # initialize when creating a chain
        self.blocks = [self.get_genesis_block()]
        self.DIFFICULTY = 4

    @staticmethod
    def get_genesis_block():
        return MinimalBlock(index="UNIQUE GENESIS BLOCK INDEX",
                            timestamp=time.time(),
                            data=None,
                            previous_hash=None)

    def add_mined_block(self, index, data, timestamp):
        self.blocks.append(MinimalBlock(index=index,
                                        timestamp=timestamp,
                                        data=data,
                                        previous_hash=self.blocks[len(self.blocks) - 1].hash))

    def get_chain_size(self):  # exclude genesis block
        return len(self.blocks) - 1

    def mine_new_block(self, data):
        nonce = 0
        timestamp = time.time()

        index = self.get_chain_size()  # caching data that doesnt change to minimise mining time
        previous_hash = self.blocks[len(self.blocks) - 1].hash

        payload = {"data": data,
                   "nonce": nonce}
        while MinimalBlock(index=index,
                           timestamp=timestamp,
                           data=str(payload),
                           # previous_hash=previous_hash).hash[:self.DIFFICULTY] != "0" * self.DIFFICULTY:
                           previous_hash=previous_hash).hash[:4] != "a0a0":
            nonce += 1
            timestamp = time.time()
            payload = {"data": data,
                       "nonce": nonce}
        print("> Block mined successfully in ", nonce, " tries")
        print("> Mining time: ", - self.blocks[index - 1].timestamp + timestamp, " seconds")
        self.add_mined_block(index=index, data=payload, timestamp=timestamp)
        return

    @staticmethod
    def verify(blocks, verbose=True):  # Verification is based purely on trust that previous blocks are valid
        flag = True
        if type(blocks[0].index) == int:
            start_index = blocks[0].index
        else:
            start_index = -1
        for i in range(1, len(blocks)):
            if blocks[i - 1].index == "UNIQUE GENESIS BLOCK INDEX" and blocks[i - 1].previous_hash is None:
                if blocks[i].index == 0 and blocks[i].hash is None:  # Firs block index check
                    flag = False
                    if verbose:
                        print('Wrong index of the first block.')
            if blocks[i].index != start_index + i:
                flag = False
                if verbose:
                    print(f'Wrong block index at block {i + start_index}.')
            if blocks[i - 1].hash != blocks[i].previous_hash:
                flag = False
                if verbose:
                    print(f'Wrong previous hash at block {i + start_index}.')
            if blocks[i].hash != blocks[i].hashing():
                flag = False
                if verbose:
                    print(f'Wrong hash at block {i + start_index}.')
            if blocks[i - 1].timestamp >= blocks[i].timestamp:
                flag = False
                if verbose:
                    print(f'Backdating at block {i + start_index}.')
        return flag

    # deprecated functions staying here only for backwards compatibility
    #
    # def fork(self, head='latest'):
    #     if head in ['latest', 'whole', 'all']:
    #         return copy.deepcopy(self)  # deepcopy since they are mutable
    #     else:
    #         c = copy.deepcopy(self)
    #         c.blocks = c.blocks[0:head + 1]
    #         return c
    #
    # def get_root(self, chain_2):
    #     min_chain_size = min(self.get_chain_size(), chain_2.get_chain_size())
    #     for i in range(1, min_chain_size + 1):
    #         if self.blocks[i] != chain_2.blocks[i]:
    #             return self.fork(i - 1)
    #     return self.fork(min_chain_size)
