


import pandas as pd

def clean_data(df):
    """
    Handle missing values in the dataset .
    
    - Numeric variables --> fill with mean .

    - Categorical variables --> fill with mode .

    """

    # تحويل القيم الفارغة إلى NaN

    df = df.replace('', pd.NA)
    df = df.replace('?', pd.NA)
    df.isnull().sum()
    
    # تحديد الاعمدة التي تحتوي على missing values

    vars_with_na = [var for var in df.columns if df[var].isnull().sum() > 0]
   
    # التعامل مع كل عمود فيه نقص
    
    for var in vars_with_na:

    # حالة خاصة للـ Region
        if var == "Region":
            df[var] = df[var].fillna("Unknown")

        # إذا Numeric
        elif df[var].dtype in ['int64', 'float64']:
            mean_value = df[var].mean()
            df[var] = df[var].fillna(mean_value)

        # إذا Categorical
        else:
            mode_value = df[var].mode()[0]
            df[var] = df[var].fillna(mode_value)


    return df


