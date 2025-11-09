# 🧩 Legacy Bitcoin Address Generator (P2PKH) — Full Explanation

This script demonstrates how to **derive a Bitcoin Legacy address (P2PKH)** directly from a recovered private key using **pure Python and ECDSA** operations.  
It follows the exact procedure Bitcoin Core uses internally for generating “1…” style legacy addresses.

---

## ⚙️ Step-by-step breakdown

### 1️⃣ Generate the public key (uncompressed)

```python
sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key_hex), curve=ecdsa.SECP256k1)
vk = sk.verifying_key
public_key = b'\x04' + vk.to_string()
Converts the hex-encoded private key into a SigningKey object.

Derives its corresponding VerifyingKey (public key).

Prefixes with 0x04 → uncompressed public key format (65 bytes total).

2️⃣ Compute HASH160 (RIPEMD160(SHA256(pubkey)))
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(hashlib.sha256(public_key).digest())
hashed_pubkey = ripemd160.digest()


First, hash the 65-byte public key with SHA256.

Then apply RIPEMD-160, yielding a 20-byte HASH160 value — the cryptographic fingerprint of the key.

3️⃣ Build the address payload
prefixed_pubkey = b'\x00' + hashed_pubkey  # 0x00 for Bitcoin mainnet
checksum = hashlib.sha256(hashlib.sha256(prefixed_pubkey).digest()).digest()[:4]


Adds a network prefix:

0x00 → Mainnet Legacy (P2PKH)

0x6f → Testnet Legacy

Calculates a 4-byte checksum using double SHA-256.

4️⃣ Encode with Base58Check
address = base58.b58encode(prefixed_pubkey + checksum).decode()


The payload + checksum is encoded in Base58Check, removing ambiguous characters (0, O, I, l, etc.).

Produces the final user-facing P2PKH address (starts with 1).

🚀 Example Output
🚀 ✅ Obliczony adres P2PKH: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

🔢 Visual flow diagram
Private key (hex)
       ↓
ECDSA SigningKey → VerifyingKey
       ↓
Uncompressed public key (0x04 + XY)
       ↓
SHA256 → RIPEMD160 → HASH160(pubkey)
       ↓
0x00 + HASH160 → double SHA256 → checksum
       ↓
Base58Check encode → ✅ P2PKH address ("1...")

🧠 Why this matters

P2PKH (“Pay to Public Key Hash”) is the original Bitcoin address format, used since 2009.

Derived entirely from the elliptic-curve public key using HASH160 + Base58Check encoding.

Understanding this derivation is crucial for cryptography audits, wallet debugging, and key recovery verification.

⚠️ Ethical reminder

This script should be used only with keys you own or have explicit authorization to test.
Generating addresses from unauthorized private keys is unethical and illegal.

© 2025 — Author: [ethicbrudhack]

BTC donation address: bc1q4nyq7kr4nwq6zw35pg0zl0k9jmdmtmadlfvqhr
