from typing import Annotated
from pydantic import BaseModel, Field, conlist, field_validator

ScoreField = Annotated[float, Field(default=0, ge=0, le=100)]

class PredictionRequest(BaseModel):
    uiux: ScoreField
    programming: ScoreField
    operational: ScoreField
    datascience: ScoreField
    cybersec: ScoreField
    qa: ScoreField
    network: ScoreField

    def normalize_scores(self):
        for field in self.model_fields:
            current_value = getattr(self, field)
            setattr(self, field, round(current_value / 100, 4))