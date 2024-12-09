## **WINE QUALITY CLASSIFICATION**

**Table of Contents**
1. Project Overview
2. Features
3. Technologies Used
4. Installation
5. Usage
6. Data
7. Model
8. Evaluation
9. Future Enhancements
10. Contributing
11. Contact

**BUSINESS PROBLEM**

The goal of the wine quality classification project is to help businesses in the wine industry (such as wineries, distributors, retailers, and quality control labs) assess and predict the quality of wines based on various chemical and sensory attributes.

The business problem can be framed as follows:

**Quality Assurance and Control:** Wineries face challenges in ensuring the consistent quality of their wine products. There might be variations in the quality of wine produced from batch to batch due to differences in grape harvest, processing conditions, and storage practices.

**Consumer Preference Matching:** Retailers and distributors need a reliable way to categorize wines into quality classes to match consumer preferences and price points. Consumers may have varying preferences based on wine quality, and a business may struggle to provide the right products that meet market demand.

**Operational Efficiency in Production:** Understanding the quality of wine based on certain chemical properties allows wineries to adjust their production process (e.g., fermentation time, sugar levels, sulfur dioxide usage) to optimize product quality, thereby reducing waste and increasing profitability.

**BUSINESS OBJECTIVE**

**Predict Wine Quality Accurately:**
Objective: To develop a predictive model that classifies wines into different quality categories (e.g., low, medium, high) based on various chemical features (e.g., acidity, alcohol, sulfur levels).

Benefit: Accurate predictions will allow wineries to categorize wines early in the production process, enabling better quality control and reducing the likelihood of substandard batches.

**Enhance Product Consistency:**
Objective: To use classification results to monitor and control wine quality over time, ensuring that the final product meets the desired standard.

Benefit: This will help wineries maintain consistent quality, leading to improved brand reputation, reduced customer complaints, and greater customer loyalty.

**Optimize Wine Production and Costs:**
Objective: By understanding the relationship between chemical properties and wine quality, wineries can optimize their production methods to reduce costs and increase yield while ensuring high-quality products.

Benefit: This can help businesses reduce unnecessary expenses (e.g., excess ingredients, energy, and resources) and focus on producing wines that meet market demand.

**Enhance Consumer Experience and Increase Sales:**
Objective: To classify wines based on quality and match them with appropriate consumer preferences, marketing strategies, and price points.

Benefit: Improved wine selection tailored to customer preferences can drive higher sales, attract more customers, and allow for better segmentation of the market (e.g., premium vs. budget wines).

**Improve Marketing and Branding Strategies:**
Objective: To leverage wine quality classification insights for more effective marketing strategies and branding efforts (e.g., premium labeling for higher-quality wines).

Benefit: Better-targeted marketing campaigns can enhance the brand’s position in the market, increase brand loyalty, and attract more consumers willing to pay a premium for high-quality wines.

**Regulatory Compliance and Certification:**
Objective: In some regions, there are strict regulations on wine labeling and classification. The model could be used to ensure that wine batches meet specific quality criteria for legal and regulatory standards.

Benefit: Meeting regulatory standards will avoid penalties and ensure that wines are properly classified for export or sale within the country.

**KPIs (Key Performance Indicators) for Success**
Prediction Accuracy: The percentage of correct predictions made by the wine quality classification model.

Operational Efficiency: Reduction in defects, waste, and production costs based on better classification and quality control.

Sales Growth: Increase in sales due to better matching of wines to consumer preferences and targeted marketing.

Customer Satisfaction: Improvements in customer satisfaction and reviews based on better product offerings.

Regulatory Compliance: Adherence to wine quality regulations and certifications.

**DATA UNDERSTANDING:**
Source of the Data The dataset for this project was obtained from Kaggle. It contains physicochemical properties of wines and their corresponding quality scores. These quality scores range from a numerical scale and are based on sensory data collected by wine experts.

Dataset Description Total Samples: [Mention the total number of rows in the dataset]. Features: The dataset includes several physicochemical properties of wine, such as:

1. Fixed Acidity
2. Volatile Acidity
3. Citric Acid
4. Residual Sugar
5. Chlorides
6. Free Sulfur Dioxide
7. Total Sulfur Dioxide
8. Density
9. pH
10. Sulphates
11. Alcohol
**Target Variable:** Quality – This represents the wine's quality score, rated between 3 and 6.

**Features**
1. Predictive Model: Uses machine learning to predict credit scores.
2. Data Preprocessing: Includes handling missing data, outliers, and scaling features.
3. Model Explainability: Provides insights into the model's decisions using feature importance.
4. Performance Metrics: Accuracy, Precision, Recall, F1-Score, and AUC-ROC.

**Technologies Used**
1. Programming Language: Python 3.13
2. Libraries:
3. Pandas
4. NumPy
5. Scikit-learn
6. Matplotlib & Seaborn for visualization

**EDA**

![image](https://github.com/user-attachments/assets/252e1a52-5e8c-4d32-983a-f4758833e439)

Imbalanced target column

![image](https://github.com/user-attachments/assets/fad36869-b038-4140-b6b1-4443c0df89cf)

Relationship between total sulfur dioxide and free sulfur dioxide on the quality of wine.

**Models**
Trained data on 3 classification models:
1. Logistic Regression
2. RandomForest Classifier
3. KNearest Neighbor

**Evaluate:**
![image](https://github.com/user-attachments/assets/914cdc62-90f6-4ca6-ab12-e6694a573419)

This is an evaluation of how the 3 models performed on all 7 classes.

**Results:**
![image](https://github.com/user-attachments/assets/68cd8507-2877-4f04-a20b-8d292162d9c0)

**Future Enhancements**
Incorporate more diverse datasets for robustness. Implement deep learning models. Develop a user-friendly web interface for real-time wine quality classification. Contributing Contributions are welcome! Please fork the repository and submit a pull request.

**Contact**
For any inquiries, please contact: wahomeshiko@gmail.com



