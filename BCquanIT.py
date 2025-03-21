import hashlib
from datetime import datetime, timedelta
class Block : 
    def __init__ (self,data ) : 
        self.data = data 
        self.hash = ""
        self.prev_hash= ""
        self.nonce = 0
        self.totaltime = ""
def compute_hash(block) : 
        data = block.data + block.prev_hash + str(block.nonce)
        data = data.encode('utf-8') # chuyen string sang bytes 
        return hashlib.sha256(data).hexdigest()
class block_chain : 
        def __init__ (self) : 
            self.chain = [] 
            block = Block("genesis block")
            start = datetime.now()
            while compute_hash(block).startswith("00000") == False : 
                block.nonce = block.nonce + 1 
                block.hash = compute_hash(block)
            end = datetime.now()
            block.totaltime = str(end -start)    
            self.chain.append(block) 
        def add_block(self,data):
             block = Block(data)
             block.prev_hash = self.chain[-1].hash 
             block.hash = compute_hash(block)
             start = datetime.now()
             while compute_hash(block).startswith("00000") == False : 
                block.nonce = block.nonce + 1 
                block.hash = compute_hash(block)
             end = datetime.now()
             block.totaltime = str(end -start)
             self.chain.append(block)
        def print_block (self):
             for block in self.chain:
                  print ( "data :", block.data)
                  print("previous hash :", block.prev_hash)
                  print ( "hash :", block.hash)
                  print ( " nonce : ", block.nonce)
                  print ("time", block.totaltime)
                  print()
        def is_valid(self) : 
            for  i in range (1,len(self.chain)) : 
                current_block = self.chain[i] 
                prev_block = self.chain[i-1]
                if compute_hash(current_block) != current_block.hash : 
                    return False 
                if prev_block.hash != current_block.prev_hash :
                    return False    
            return True                 
blockchain = block_chain() 
blockchain.add_block("tran tuan dung")
blockchain.add_block("nguyen thuy van ")
blockchain.add_block("nguyen van A ") 
 
#blockchain.chain[1].data = " Tran Dung"
#blockchain.chain[1].hash = compute_hash(blockchain.chain[1])
blockchain.print_block() 
print("is valid ? ", blockchain.is_valid())

                 