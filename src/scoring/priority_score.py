
from src.config import WEIGHTS
from src.models.predict import get_priority_level

def calculate_priority_score(df):
    """
    Calculate priority score based on predefined weights.
    """

    # حساب الـ score
    df['PriorityScore'] = (
        df['SpecialCase'] * WEIGHTS['special_case'] +
        df['Income'] * WEIGHTS['income'] +
        df['FamilyMembers'] * WEIGHTS['family_size'] +
        df['Housing'] * WEIGHTS['housing']
    )

    # تحديد مستوى الأولوية
    df['PriorityLevel'] = df['PriorityScore'].apply(get_priority_level)

    return df