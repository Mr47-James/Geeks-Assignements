brand = dict(
    name="Zara",
    create_date=1975,
    creator_name="Amancio Ortega Gaona",
    type_of_clothes=["men", "women", "children", "home"],
    international_competitors=["Gap", "H&M", "Benetton"],
    number_stores=7000,
    major_color={"France": "blue", "Spain": "red", "US": ["pink", "green"]}
)

brand["number_stores"] = 2
print(f"The Zara Targeted Clients Are {brand.get('type_of_clothes')}")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:   
    brand["international_competitors"] = "Desigual"
    brand.pop("create_date")  
    print(brand["international_competitors"])
    print(brand.keys())
    brand["more_on_zara"] = {"creation_date": 1975, "number_stores": 10000}
    print(brand.get("number_stores"))
