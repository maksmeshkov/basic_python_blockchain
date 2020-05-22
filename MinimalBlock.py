import hashlib


class MinimalBlock():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashing()

    def hashing(self):
        string = f"{self.index}{self.timestamp}{str(self.data)}{self.previous_hash}{self.timestamp}"
        return hashlib.sha256(string.encode("utf-8")).hexdigest()

    def block_info(self):
        info = {"block_index": self.index, "block_timestamp": self.timestamp, "block_data": self.data,
                "block_previous_hash": self.previous_hash, "block_hash": self.hash}
        return info
