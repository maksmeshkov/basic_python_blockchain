from MinimalChain import MinimalChain


MicroChain = MinimalChain()

data = "Doomguy pays Booster_dealer 3btc" \
       "Demon_slayer228 pays Physical_storage_dealer 13.345btc"
for i in range(10):
    MicroChain.mine_new_block(data=data)

    blocks = MicroChain.blocks[-2], MicroChain.blocks[-1]
    print("> Running block verification submodule...")
    if MicroChain.verify(blocks=blocks) == True:
        print("> Verification complete. No payload tamper detected.")
    print()
    print()

chain_length = MicroChain.get_chain_size()
for i in range(chain_length+1):
    print(MicroChain.blocks[i].block_info())