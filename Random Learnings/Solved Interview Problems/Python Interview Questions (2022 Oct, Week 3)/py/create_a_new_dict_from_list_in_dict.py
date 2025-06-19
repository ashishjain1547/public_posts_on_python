example = {"a":1,"b":[1,2]}

iter = example.get("b")

new_list = []

for p in iter:
    print(f"p is {p}")
    tmp_dict = dict(example)
    tmp_dict["b"] = p
    print(tmp_dict)
    new_list.append(tmp_dict)

print(new_list)