from mongoengine import *

from app.models import BaseModel


class FridgeModel(BaseModel):
    meta = {
        'collection': 'fridge'
    }

    # uuid
    id = StringField(
        primary_key=True
    )
    pw = StringField(
        required=True,
        min_length=4,
        max_length=8
    )
    name = StringField(
        required=True,
        min_length=3,
        max_length=18
    )


class FridgeSectionModel(BaseModel):
    meta = {
        'collection': 'section'
    }

    # "fridge_id.id" 의 형태
    id = StringField(
        primary_key=True
    )
    fridge = ReferenceField(
        required=True,
        document_type='FridgeModel',
        reverse_delete_rule=CASCADE
    )
    name = StringField(
        required=True,
        min_length=2,
        max_length=11
    )


class FoodModel(BaseModel):
    meta = {
        'collection': 'food'
    }

    # "fridge_id.section_id.id" 의 형태
    id = StringField(
        primary_key=True
    )
    fridge = ReferenceField(
        required=True,
        document_type='FridgeModel',
        reverse_delete_rule=CASCADE
    )
    section = ReferenceField(
        required=True,
        document_type="FridgeSectionModel",
        reverse_delete_rule=CASCADE
    )
    name = StringField(
        required=True
    )
    category = StringField(
        required=True
    )
    expiration_date = DateTimeField(
        required=True
    )
    memo = StringField(
        default='',
        max_length=100
    )
    label = StringField(
        default='white'
    )
    is_black = BooleanField(
        default=False
    )
    ordering_number = IntField(
        required=True,
        default=0
    )

# -Category-
# grain 곡물
# potatoes_starch 감자 및 전분
# sugars 당류
# fabaceae 두류
# nuts 견과류
# vegetables 채소류
# mushroom 버섯류
# fruit 과실류
# meat 고기류
# egg 난류
# seafood 어패류
# seaweed 해조류
# milk 유제품
# oil 유지류
# Beverages 음료 및 주류
# seasoning 조미료
# cooked_processed 조리 및 가공류
# ect 기타

# -Label-
# white - 라벨 없음
