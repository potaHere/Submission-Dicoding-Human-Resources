import joblib
import numpy as np

# Load the trained model
model = joblib.load('HR-model.pkl')

# Example input data for prediction
input_data = np.array([[
    41,              # Age
    2,               # BusinessTravel (encoded)
    3,               # Department (encoded)
    1,               # DistanceFromHome
    4,               # Education
    2,               # EducationField (encoded)
    65,              # EnvironmentSatisfaction
    3,               # Gender (encoded)
    3,               # JobInvolvement
    2,               # JobLevel
    7,               # JobRole (encoded)
    3,               # JobSatisfaction
    1,               # MaritalStatus (encoded)
    3,               # MonthlyIncome
    2,               # NumCompaniesWorked
    0,               # Over18 (encoded)
    3,               # OverTime (encoded)
    15,              # PercentSalaryHike
    3,               # PerformanceRating
    2,               # RelationshipSatisfaction
    80,              # StockOptionLevel
    6,               # TotalWorkingYears
    3,               # TrainingTimesLastYear
    2,               # WorkLifeBalance
    10,              # YearsAtCompany
    6,               # YearsInCurrentRole
    5,               # YearsSinceLastPromotion
    8,               # YearsWithCurrManager
    0.5,             # StandardHours (likely standardized)
    0.7,             # Employee's Worth
    0.8,             # TeamDynamics
    0.6,             # SkillDevelopment
    0.9              # CareerGrowth
]])
# Make predictions
predictions = model.predict(input_data)
# Print the predictions
print(f"Predicted Attrition (Untuk label sesungguhnya): {'Yes' if predictions[0] == 1 else 'No'}")