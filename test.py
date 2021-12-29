import secp256k1 as ice
print(ice.privatekey_to_h160(0, True, 0x1).hex())
print(ice.privatekey_to_h160(0, True, 0x2).hex())
# # res bcfeb728b584253d5f3f70bcb780e9ef218a68f4
# P = ice.scalar_multiplication(1)
# print(ice.pubkey_to_h160(0, True, P).hex())
print(ice.privatekey_loop_h160_sse(10, 0, True, 1)[0:20].hex())
print(ice.privatekey_loop_h160_sse(10, 0, True, 1)[20:40].hex())
seearch = "751e76e8199196d454941c45d1b3a323f1433bd6"
searchbyte = bytes.fromhex(seearch)
col = ice.privatekey_loop_h160_sse(1000000, 0, True, 2)
print("search..",len(col))
if searchbyte in col:
    print("yes")
for n in range(0,len(col),20):
    print(n)