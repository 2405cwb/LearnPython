# author: cwb
# date: 2025/1/20
import hashlib
import os
# 要哈希的数据
data = "Hello, World!"

# 创建哈希对象
hash_md5 = hashlib.md5()
hash_sha256 = hashlib.sha256()

# 更新哈希对象
hash_md5.update(data.encode('utf-8'))
hash_sha256.update(data.encode('utf-8'))

# 获取哈希值
print("MD5:", hash_md5.hexdigest())
print("SHA256:", hash_sha256.hexdigest())


# 生成随机盐
salt = os.urandom(16)  # 16 字节的随机盐

# 密码
password = "my_password"

# 加盐哈希
hash_sha256 = hashlib.sha256()
hash_sha256.update(salt + password.encode('utf-8'))
hashed_password = hash_sha256.hexdigest()

print("Salt:", salt.hex())
print("Hashed Password:", hashed_password)

# 查看支持的哈希算法
print(hashlib.algorithms_available)

'''
 MD5 和 SHA1 的安全性：MD5 和 SHA1 已经被认为是不安全的哈希算法，不建议用于密码存储或数据完整性校验。
使用更安全的算法：推荐使用 SHA256、SHA512 或更安全的算法（如 SHA3、BLAKE2）。

加盐哈希：在密码存储中，务必使用加盐哈希来增加安全性。
'''