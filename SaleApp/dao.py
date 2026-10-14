import json

def load_categories():
    with open("data/cate.json", encoding="utf-8") as f:
        return json.load(f)

def load_products(q=None, cate_id=None):
    with open("data/products.json", encoding="utf-8") as f:
        prods = json.load(f)
        if q:
            prods = [p for p in prods if q in p["name"]]
        if cate_id:
            prods = [p for p in prods if cate_id == p["cate_id"]]
        return prods

if __name__=="__main__":
    print(load_categories())