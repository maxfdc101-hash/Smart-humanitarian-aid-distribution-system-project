
import pandas as pd 
from src.config import HOUSING_MAPPING


    #==============================
    # Transform income
    #==============================

def transform_income(x):
   if x < 1000:
      return 1
      
   elif x < 2000 :
      return 0.5
      
   else :
      return 0

   

 # ========================================
 #  Family size (custom Transformation)
 # =========================================
def family_size_score(size):
      if size < 3 :

         return 0.2 
      
      elif 3 <= size <= 7 :

         return 0.5
      
      elif 7 < size <= 10 :

         return 0.7
      
      else:

         return 1
      




def feature_engineering(df):
    """
    Apply feature transformations:
    - Binary encoding
    - ordinal encoding 
    - one-hot encoding 
    - custom transformations
    """

    # ============================
    # 1. special case (Binary)
    # ============================
    # يفترض انه 0 , 1 بالفعل , فقط تأكيد   
     
    df['SpecialCase'] = df['SpecialCase'].astype(int) 

    # =============================
    # 2. Housing (ordinal encoding)
    # ==============================
    if df['Housing'].dtype == 'object':
       df['Housing'] = df['Housing'].astype(str).str.strip()
       df['Housing'] = df['Housing'].map(HOUSING_MAPPING)

    # ========================================
    # 3. Family size (custom transformation)
    # ========================================

    df['FamilyMembers'] = df['FamilyMembers'].apply(family_size_score)


    # ========================================
    # 4. Income (custom transformation)
    # ========================================

    df["Income"] = df["Income"].apply(transform_income)

    # ========================================
    # 5. Region (one_hot encodin)
    # =========================================  
    if 'Region' in df.columns:
        df = pd.get_dummies(df, columns=['Region'], drop_first=True)

    return df 

   
   

