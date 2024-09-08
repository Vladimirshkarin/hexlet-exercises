from hexlet_exercises.oop_design.collection import Collection


# BEGIN (write your solution here)
def format(raw):
    for item in raw:
        item["name"] = item["name"].strip().lower()
        item["country"] = item["country"].strip().lower()
    inner = Collection(raw)
    grouped = (
        inner.unique()
        .sort_by(lambda x: (x["country"], x["name"]))
        .group_by(lambda x: (x["country"], x["name"]))
    )
    return grouped.all()
# END


# BEGIN reference solution
def format_ref(data):
    c = Collection(data)
    return (
        c.map_(_normalise)
        .unique()
        .group_by(lambda row: (row["country"], row["name"]))
        .map_(lambda row: {key: sorted(values) for key, values in row.items()})
        .sort_by(lambda row: list(row.keys()))
        .all()
    )


def _normalise(row):
    return {
        "name": row["name"].lower().strip(),
        "country": row["country"].lower().strip(),
    }
# END reference solution
