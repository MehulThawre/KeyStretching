# Key Stretching with SHA-256

This project implements Key Stretching using SHA-256 to enhance password security. It applies multiple iterations of SHA-256 hashing with a random salt to make brute-force attacks more difficult.

## Features
- Uses SHA-256 for secure hashing.
- Adds a random salt to prevent rainbow table attacks.
- Supports iterations (default) to slow down brute-force attempts.
- Simple and easy-to-use Python implementation.

---

## Installation

1. Clone the repository:
```sh
git clone https://github.com/MehulThawre/KeyStretching.git
cd KeyStretching
```

2. Install Python (if not installed):  
- [Download Python](https://www.python.org/downloads/) and install it.

3. Run the script:
```sh
python main.py
```

---

##  Usage

1. Run the script and enter a password.
2. The program will generate:
   - A random salt.
   - A key-stretched hash after 100,000 SHA-256 iterations.

Example Output:
```
Enter your password: mysecurepassword123
Salt: 7f8c71e89444d2fbc2d9e8c2c35b0d1e
Key-Stretched Hash: e1a5f0be32f47f869f68b46a2b63986bd5ff66e4e3c716b80df48a17ebea313f
```

---

## Why Use Key Stretching?
✔ Prevents brute-force attacks by increasing hashing time.  
✔ Prevents rainbow table attacks by adding a unique random salt.  
✔ Used in security standards like PBKDF2, bcrypt, and scrypt.  

---

## Contributing
Want to improve the project? Follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-new
   ```
3. Commit your changes:
   ```sh
   git commit -m "Added a new feature"
   ```
4. Push to GitHub:
   ```sh
   git push origin feature-new
   ```
5. Open a Pull Request.




🎉 Happy Hashing! Stay Secure! 🔐

