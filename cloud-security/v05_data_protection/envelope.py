# Envelope encryption with a toy cipher (teaching only: never use XOR for real)
import hashlib
def stream(key, n):
    out, i = b"", 0
    while len(out) < n:
        out += hashlib.sha256(key + i.to_bytes(4, "big")).digest(); i += 1
    return out[:n]
def xor(key, data):
    return bytes(a ^ b for a, b in zip(data, stream(key, len(data))))
kms = {"kek-v1": b"master-one", "kek-v2": b"master-two"}  # stays in KMS
dek = b"data-key-for-file-17"                     # one data key per file
report = b"MRI report 4471: no fracture seen"
blob = xor(dek, report)                           # the file, encrypted locally
wrapped = ("kek-v1", xor(kms["kek-v1"], dek))     # data key, wrapped by KMS
print("stored file   :", blob[:10].hex(), "...")
print("stored key    :", wrapped[0], wrapped[1][:5].hex(), "...")
plain_dek = xor(kms[wrapped[0]], wrapped[1])      # ask KMS to unwrap it
print("read back     :", xor(plain_dek, blob).decode())
wrapped = ("kek-v2", xor(kms["kek-v2"], plain_dek))   # rotate: re-wrap only
print("rotated to", wrapped[0], "| file unchanged:", blob == xor(dek, report))
del kms["kek-v2"]                                 # destroy the master key
print("key destroyed | file readable:", wrapped[0] in kms)
