
# ==============================
# Feature Weights
# ==============================

WEIGHTS = {
    "special_case" : 0.4 ,
    "income" : 0.3 ,
    "family_size" : 0.2 ,
    "housing" : 0.1

}

# ================================
# Income Categories ( if used)
# ================================

INCOME_MAPPING = {
    "low" : 1,
    "medium" : 0.5,
    "high" : 0
}

# ============================
# Housing Encoding (ordinal)
# ============================

HOUSING_MAPPING = {
    "مدمر بالكامل": 1,
    "مدمر جزئيا": 0.7,
    "ايجار": 0.4,
    "مخيم ايواء/خيمة": 0.2
}





