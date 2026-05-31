
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
    "سيئ" : 1,
    "جيد" : 0.7,
    "جيد جدا" : 0.2
}


# # ==========================
# # Family Size Intervals
# # ==========================

# def family_size_score(size):
#     if size < 3 :

#         return 0.2 
    
#     elif 3 <= size <= 7 :

#         return 0.5
    
#     elif 7 < size <= 10 :

#         return 0.7
    
#     else:

#         return 1
    

# # =============================
# # priority levels
# # =============================

# def get_priority_level(score):
#     if score >= 0.7 :

#         return "High"
    
#     elif score >= 0.4 :

#         return "Medium"
    
#     else :

#         return "Low"


