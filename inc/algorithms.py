validalgs = {   '': 'select algo type...',
    '0': 'MD5',
    '10': 'md5($plaintext.$salt)',
    '100': 'SHA1',
    '1000': 'NTLM',
    '10000': 'Django (PBKDF2-SHA256)',
    '101': 'nsldap, SHA-1(Base64), Netscape LDAP SHA',
    '104': 'SHA1.Substr(0, 32)',
    '10400': 'PDF 1.1 - 1.3 (Acrobat 2 - 4)',
    '10410': 'PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #1',
    '10420': 'PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #2',
    '10500': 'PDF 1.4 - 1.6 (Acrobat 5 - 8)',
    '10600': 'PDF 1.7 Level 3 (Acrobat 9)',
    '10700': 'PDF 1.7 Level 8 (Acrobat 10 - 11)',
    '10800': 'SHA384',
    '10900': 'PBKDF2-HMAC-SHA256',
    '11': 'Joomla < 2.5.18',
    '110': 'sha1($plaintext.$salt)',
    '11300': 'Bitcoin/Litecoin wallet.dat',
    '11600': '7-Zip',
    '11900': 'PBKDF2-HMAC-MD5',
    '120': 'sha1($salt.$plaintext)',
    '12000': 'PBKDF2-HMAC-SHA1',
    '12001': 'Atlassian (PBKDF2-HMAC-SHA1)',
    '121': 'SMF (Simple Machines Forum) > v1.1',
    '12100': 'PBKDF2-HMAC-SHA512',
    '124': 'Django (SHA-1)',
    '12500': 'RAR3-hp (*0* only)',
    '12700': 'Blockchain, My Wallet',
    '12900': 'Android FDE (Samsung DEK)',
    '130': 'sha1(utf16le($plaintext).$salt)',
    '1300': 'SHA224',
    '13000': 'RAR5',
    '13200': 'AxCrypt',
    '13300': 'AxCrypt in-memory SHA1',
    '13400': 'KeePass 1 (AES/Twofish) and KeePass 2 (AES)',
    '13800': 'Windows Phone 8+ PIN/plaintext',
    '13900': 'OpenCart',
    '140': 'sha1($salt.utf16le($plaintext))',
    '1400': 'SHA256',
    '1410': 'sha256($plaintext.$salt)',
    '1420': 'sha256($salt.$plaintext)',
    '14400': 'sha1(CX)',
    '14600': 'LUKS',
    '14700': 'iTunes backup < 10.0',
    '14800': 'iTunes backup >= 10.0',
    '15200': 'Blockchain, My Wallet, V2',
    '15600': 'Ethereum Wallet, PBKDF2-HMAC-SHA256',
    '15700': 'Ethereum Wallet, SCRYPT',
    '1600': 'Apache $apr1$ MD5, md5apr1, MD5 (APR)',
    '16200': 'Apple Secure Notes',
    '16300': 'Ethereum Pre-Sale Wallet, PBKDF2-HMAC-SHA256',
    '16600': 'Electrum Wallet (Salt-Type 1-3)',
    '16700': 'FileVault 2',
    '16800': 'WPA-PMKID-PBKDF2',
    '1700': 'SHA512',
    '1710': 'sha512($plaintext.$salt)',
    '1720': 'sha512($salt.$plaintext)',
    '17200': 'PKZIP (Compressed)',
    '17210': 'PKZIP (Uncompressed)',
    '17220': 'PKZIP (Compressed Multi-File)',
    '17225': 'PKZIP (Mixed Multi-File)',
    '17230': 'PKZIP (Compressed Multi-File Checksum-Only)',
    '17700': 'Keccak-224',
    '17800': 'Keccak-256',
    '17900': 'Keccak-384',
    '1800': 'sha512crypt $6$, SHA512 (Unix)',
    '18000': 'Keccak-512',
    '18300': 'Apple File System (APFS)',
    '18900': 'Android Backup',
    '19500': 'Ruby on Rails Restful-Authentication',
    '20': 'md5($salt.$plaintext)',
    '20011': 'DiskCryptor SHA512 + XTS 512 bit (AES/Twofish/Serpent)',
    '20012': 'DiskCryptor SHA512 + XTS 1024 bit (AES-Twofish/Twofish-Serpent/Serpent-AES)',
    '20013': 'DiskCryptor SHA512 + XTS 1536 bit (AES-Twofish-Serpent)',
    '20710': 'sha256(sha256($plaintext).$salt)',
    '20711': 'AuthMe sha256',
    '20800': 'sha256(md5($plaintext))',
    '20900': 'md5(sha1($plaintext).md5($plaintext).sha1($plaintext)) ',
    '21': 'osCommerce, xt:Commerce',
    '2100': 'Domain Cached Credentials 2 (DCC2), MS Cache 2',
    '21100': 'sha1(md5($plaintext.$salt))',
    '21200': 'md5(sha1($salt).md5($plaintext))',
    '21300': 'md5($salt.sha1($salt.$plaintext))',
    '21700': 'Electrum Wallet (Salt-Type 4)',
    '21800': 'Electrum Wallet (Salt-Type 5)',
    '220': 'sha1DASH sha1(--$salt--$plaintext--)',
    '22000': 'WPA-PBKDF2-PMKID+EAPOL',
    '22100': 'BitLocker',
    '22300': 'sha256($salt.$plaintext.$salt)',
    '22301': 'Telegram client app passcode (SHA256)',
    '22500': 'MultiBit Classic .key (MD5)',
    '2500': 'WPA/WPA2',
    '2501': 'WPA/WPA2 PMK',
    '2600': 'md5(md5($plaintext))',
    '2611': 'vBulletin < v3.8.5',
    '2612': 'PHPS',
    '2711': 'vBulletin >= v3.8.5',
    '2811': 'MyBB 1.2+, IPB2+ (Invision Power Board)',
    '300': 'MySQL4.1/MySQL5',
    '3000': 'LM',
    '3200': 'bcrypt $2*$, Blowfish (Unix)',
    '400': 'phpass, phpBB3 (MD5), Joomla >= 2.5.18 (MD5), WordPress (MD5)',
    '50': 'HMAC-MD5 (key = $plaintext)',
    '500': 'md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5), Cisco-IOS $1$ (MD5)',
    '5100': 'Half MD5',
    '60': 'HMAC-MD5 (key = $salt)',
    '6100': 'Whirlpool',
    '6600': '1Password, agilekeychain',
    '7100': 'macOS v10.8+ (PBKDF2-SHA512)',
    '7400': 'sha256crypt $5$, SHA256 (Unix)',
    '7900': 'Drupal7',
    '8800': 'Android FDE <= 4.3',
    '8900': 'scrypt',
    '900': 'MD4',
    '9200': 'Cisco-IOS $8$ (PBKDF2-SHA256)',
    '9300': 'Cisco-IOS $9$ (scrypt)',
    '9400': 'MS Office 2007',
    '9500': 'MS Office 2010',
    '9600': 'MS Office 2013',
    '9700': 'MS Office <= 2003 $0/$1, MD5 + RC4',
    '9710': 'MS Office <= 2003 $0/$1, MD5 + RC4, collider #1',
    '9720': 'MS Office <= 2003 $0/$1, MD5 + RC4, collider #2',
    '9800': 'MS Office <= 2003 $3/$4, SHA1 + RC4',
    '9810': 'MS Office <= 2003 $3, SHA1 + RC4, collider #1',
    '9820': 'MS Office <= 2003 $3, SHA1 + RC4, collider #2'
}