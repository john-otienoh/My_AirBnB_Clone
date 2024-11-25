from models.base_model import BaseModel

class State(BaseModel):
    """class that inherit from BaseModel:"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new State instance"""
        super().__init__(*args, **kwargs)
        