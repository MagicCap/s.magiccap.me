from tables import LinkShortener

if not LinkShortener.exists():
    LinkShortener.create_table()
