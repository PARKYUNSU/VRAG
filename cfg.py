class Config:
    def __init__(self):
        self.download_path = "./images"
        self.imgs_per_category = 300
        self.milvus_uri = "milvus.db"
        self.collection_name = "cir_demo_large"
        self.device = "mps"
        self.model_type = "large"
        self.model_path = "./models/magic_lens_clip_large.pkl"
        self.api_type = "openai"