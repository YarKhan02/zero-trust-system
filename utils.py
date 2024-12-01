from data import decrypt_data

def mask_account_number(account_number):
    decrypted = decrypt_data(account_number)
    return f"****{decrypted[-4:]}"

def anonymize_amount(amount):
    decrypted = decrypt_data(amount)
    return f"${float(decrypted):.0f}"
