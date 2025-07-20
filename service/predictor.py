import numpy as np
from model.model_loader import model
from app.data.materials import materials_mapping

categories = [
    "UI/UX", "Programming", "Operational",
    "Data Science", "CyberSecurity", "Quality Assurance", "Computer Network"
]

def predict(scores: list, top_k: int = 3):
    new_data = np.expand_dims(scores, axis=0)
    new_data = np.expand_dims(new_data, axis=1)
    new_data_prediction = model.predict(new_data)[0]

    threshold = float(np.mean(new_data_prediction))
    above_threshold = [
        {"category": categories[i], "probability": float(prob)}
        for i, prob in enumerate(new_data_prediction)
        if prob > threshold
    ]

    if above_threshold:
        above_threshold.sort(key=lambda x: x["probability"], reverse=True)
        result = above_threshold[:top_k]
    else:
        top_index = int(new_data_prediction.argmax())
        result = [{
            "category": categories[top_index],
            "probability": float(new_data_prediction[top_index])
        }]

    for item in result:
        category = item["category"]
        item["material"] = materials_mapping.get(category, {})

    return {
        "threshold": threshold,
        "result": result
    }
