# Create a secure random number

The [secrets](https://docs.python.org/3/library/secrets.html) module can be used to create cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

```
import secrets
secrets.token_hex()
```