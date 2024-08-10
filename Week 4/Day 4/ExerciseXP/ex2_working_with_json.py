import json

sampleJson = {
    "company": {"employee": {"name": "emma", "payable": {"salary": 7000, "bonus": 800}}}
}

salary_info = sampleJson["company"]["employee"]["payable"]
print("Salary: ", salary_info["salary"])

sampleJson["birth_date"] = {}
sampleJson["birth_date"]["year"] = 1990
print(sampleJson)

json_file = "my_file.json"

with open(json_file, "w") as file_obj:
    json.dump(sampleJson, file_obj, indent=2)
    print(f"'{json_file}' created")
