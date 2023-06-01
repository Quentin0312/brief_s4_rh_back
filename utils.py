def toJson(datas, model):
    model_fields = [column.name for column in model.__table__.columns]
    json = []

    for data in datas:
        model = {}
        for field in model_fields:
            model[field] = getattr(data, field)
        json.append(model)

    return json
