import os
import json

import dotenv

dotenv.load_dotenv()


TG_CHANNEL: str = os.getenv("VAR_TG_CHANNEL", "@Today_in_Russia")
TG_BOT_TOKEN: str = os.getenv("VAR_TG_BOT_TOKEN", "5534251891:AAH0El5famG0atIM03qpallJr8VTBeLcSPQ")
VK_TOKEN: str = os.getenv("VAR_VK_TOKEN", "vk1.a.9kS6q7hsgD3O6HaMXENVMLsb-hXi0WkGVitW3cBZIKMvGO31r3FR351Lt7QV7iDxQh6Q00xVWne5g4F7H4Mt23abUhYIiGTZB40ya0ynTGtKfP3bHJouHIyItPamHpx4xVo1_O-pc53cbykqdBSlpUslpBe1vIekz5PopeOQGgHaT6q3Tgu-1NhAWC_Lr7Im")
VK_DOMAIN: str = os.getenv("VAR_VK_DOMAIN", "vesti")

REQ_VERSION: float = float(os.getenv("VAR_REQ_VERSION", 5.103))
REQ_COUNT: int = int(os.getenv("VAR_REQ_COUNT", 3))
REQ_FILTER: str = os.getenv("VAR_REQ_FILTER", "owner")

SINGLE_START: bool = os.getenv("VAR_SINGLE_START", "").lower() in ("true",)
TIME_TO_SLEEP: int = int(os.getenv("VAR_TIME_TO_SLEEP", 120))
SKIP_ADS_POSTS: bool = os.getenv("VAR_SKIP_ADS_POSTS", "").lower() in ("true",)
SKIP_COPYRIGHTED_POST: bool = os.getenv("VAR_SKIP_COPYRIGHTED_POST", "").lower() in ("true")
SKIP_REPOSTS: bool = os.getenv("VAR_SKIP_REPOSTS", "").lower() in ("true")

WHITELIST: list = json.loads(os.getenv("VAR_WHITELIST", "[]"))
BLACKLIST: list = json.loads(os.getenv("VAR_BLACKLIST", "[]"))
