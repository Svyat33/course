def make_country(a,b):
    return {
        "name": a,
        "capital": b
    }

def print_country(d):
    print(f"Страна: {d['name']} столица: {d['capital']}" )

if __name__ == "__main__":
    d = make_country("Germany", "Berlin")
    print_country(d) 