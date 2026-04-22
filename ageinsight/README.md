## Ahmad, Erbakan, 12306435

---

### Overview

**AgeInsight** is a web-based application designed to provide insights into health and age prediction. Built using Streamlit, the app enables users to explore data trends, clean datasets, engineer features, and make age predictions with machine learning models. The project integrates data visualization, outlier handling, fake data generation, and a chatbot for user interaction.

---

### Links

- **MyGit Repository**: [Link to Repository](https://mygit.th-deg.de/ea04435/ageinsight)
- **MyGit Wiki**: [Link to Wiki](https://mygit.th-deg.de/ea04435/ageinsight/-/wikis/home)

---

### Project Description

The AgeInsight project provides a platform for:
- Visualizing dataset trends such as correlations, distributions, and outliers.
- Cleaning and transforming data for modeling.
- Generating fake data to improve model robustness.
- Training a regression model to predict the age based on health parameters.
- Using a chatbot for intuitive user interaction.

---

### Installation

#### Prerequisites
Mentioned in requirements.txt
- **Python 3.9.6**
- **Streamlit 1.41.0**
- **Pandas 1.5.0**
- **Plotly 5.15.0**
- **scikit-learn 1.0.2**
- **Matplotlib 3.4.0**
- **NumPy 1.21.0**
- **Rasa 3.0.0**

#### Steps

1. Clone the repository:
   git clone https://mygit.th-deg.de/ea04435/ageinsight

2. Navigate to the project directory:
   cd ageinsight

3. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Launch the application:
   streamlit run main.py


---

### Data

- **Source**: [Kaggle - Age Prediction Dataset](https://www.kaggle.com/datasets/pooriamst/age-prediction/data)
- **Outlier Handling**:
  - Outliers in BMI and fasting glucose levels are identified using the IQR method and replaced with the column mean.
- **Fake Data**:
  - 30% additional data is generated based on the original data's distribution with slight variations.
  - Fake data improves model generalizability.

---

### Basic Usage

1. **Start the application**:
   streamlit run main.py

2. **Key Features**:
   - Explore dataset metrics.
   - Handle outliers and add fake data.
   - Engineer features for better modeling.
   - Train and evaluate models.
   - Use the chatbot for dataset-related queries.

---

### Implementation of the Requests

1. **Outliers and Fake Data**:
   - Implemented in `03_Data_Handling.py`.
   - Fake data accounts for 30% of the dataset.
2. **Data Visualization**:
   - Histograms and scatter plots implemented in `01_Data_Metrics.py`.
3. **Machine Learning**:
   - Linear Regression and Random Forest implemented in `04_Regression_Model_Comparison.py`.
4. **Chatbot**:
   - Placeholder chatbot implemented in `07_Chat_Bot.py`. Rasa integration is pending.
5. **Feature Engineering**:
   - Log transformations and normalization implemented in `06_Feature_Engineering.py`.

---

### Work Done

#### Ahmad Erbakan
- Data handling: Outlier processing and fake data generation.
- Chatbot development.
- Visualizations and analysis.
- Use-case-driven enhancements.