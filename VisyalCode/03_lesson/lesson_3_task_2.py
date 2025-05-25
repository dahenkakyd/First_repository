from smartphone import Smartphone
catalog = [
    Smartphone ("TECNO","POVA 6 Neo","+79245678515"),
    Smartphone ("Xiaomi", "15 Pro", "+79194672843"),
    Smartphone ("Realme", "12 Pro+", "+79877694816"),
    Smartphone ("Apple","iPhone 16 Plus","+79083618487"),
    Smartphone ("Samsung", "Galaxy S25", "+79994576615")
    ]

for smartphone in catalog:
    print(f"{smartphone.name_phone}-{smartphone.model}.{smartphone.number}")