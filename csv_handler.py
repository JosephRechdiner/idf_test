import csv
import io
from entities.soldier import Soldier
from fastapi import File

def convert_csv_to_objects(file: File):
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}

    content = file.file.read().decode("utf-8")
   
    reader = csv.reader(io.StringIO(content))
    next(reader)
    rows = list(reader)

    all_soldiers = []
    for row in rows:
        new_soldier = Soldier(
            personal_number=int(row[0]),
            first_name=row[1],
            last_name=row[2],
            gender=row[3],
            city=row[4],
            distance=int(row[5])
            )
        all_soldiers.append(new_soldier)

    return all_soldiers