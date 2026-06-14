annotations = [
    {"id": 1, "label": "Car", "confidence": 0.95},
    {"id": 2, "label": "Pedestrian", "confidence": 0.88},
    {"id": 3, "label": "", "confidence": 0.91},
    {"id": 4, "label": "Traffic Light", "confidence": 1.10},
    {"id": 2, "label": "Pedestrian", "confidence": 0.88}
]

seen_ids = set()
errors = []

for item in annotations:

    if item["id"] in seen_ids:
        errors.append(f"Duplicate ID: {item['id']}")
    else:
        seen_ids.add(item["id"])

    if item["label"] == "":
        errors.append(f"Missing label for ID {item['id']}")

    if item["confidence"] < 0 or item["confidence"] > 1:
        errors.append(
            f"Invalid confidence for ID {item['id']}: {item['confidence']}"
        )

print("===== WAYMO DATA VALIDATOR =====")
print()

if len(errors) == 0:
    print("All records are valid.")
else:
    print("Validation Errors:")
    for error in errors:
        print("-", error)

print()
print("Total Records:", len(annotations))
print("Errors Found:", len(errors))
