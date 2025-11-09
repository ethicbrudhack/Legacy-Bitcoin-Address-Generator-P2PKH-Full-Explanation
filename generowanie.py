import ecdsa
import hashlib
import base58

def private_key_to_public_key(private_key_hex):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key_hex), curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    return b'\x04' + vk.to_string()  # Uncompressed public key (65 bytes)

def public_key_to_p2pkh_address(public_key):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(public_key).digest())
    hashed_pubkey = ripemd160.digest()
    prefixed_pubkey = b'\x00' + hashed_pubkey  # 0x00 for mainnet P2PKH
    checksum = hashlib.sha256(hashlib.sha256(prefixed_pubkey).digest()).digest()[:4]
    return base58.b58encode(prefixed_pubkey + checksum).decode()

# Twój odzyskany klucz prywatny
private_key_hex = "6a07dd14de5bb5d26998134a93a7f4f53f86ab04fea055bbbb3d8b0bfeae964a"

# Konwersja klucza prywatnego na publiczny i adres Legacy P2PKH
public_key = private_key_to_public_key(private_key_hex)
address_p2pkh = public_key_to_p2pkh_address(public_key)

print(f"🚀 ✅ Obliczony adres P2PKH: {address_p2pkh}")
