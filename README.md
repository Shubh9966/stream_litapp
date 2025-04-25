

# 💳 Credit Risk Prediction App

An interactive web app that predicts whether a customer is a **credit risk** (risky borrower) or not, using financial and demographic features. Built using **Streamlit**, **Scikit-learn**, and a well-crafted custom logic based on domain insights 🧠.

---

## 🚀 Live Demo

👉 Check it out here: [**Click to Open App**](https://appapp-gjwzhnvmmnhlvgkunkawgu.streamlit.app/)  
🧪 Try with different customer inputs and see the model’s prediction in real-time!

---

## 📂 Dataset

📊 Dataset used: [**German Credit Dataset (UCI / Kaggle)**](https://www.kaggle.com/datasets/uciml/german-credit/data)

Contains data of 1000 customers, labeled as **credit risk = 1 (risky)** or **0 (safe)**, based on 20+ financial and demographic attributes.

---

## ⚙️ How it Works

The app uses a **custom rule-based system** + a trained **Gradient Boosting Classifier** model.

## 🎯 Scoring Strategy – Behind the Risk Flag 🚩

To decide if a customer is **risky (`CreditRisk = 1`)** or **safe (`CreditRisk = 0`)**, a **custom rule-based scoring system** is used — just like how a loan officer manually evaluates applications.

Each customer is assigned a `risk_score`, starting from **0**. Based on certain conditions, the score is **incremented (+1)** for risky behavior and **decremented (-1)** for safe signs.

👇 Here's how it works:

---

### 💰 1. Credit Amount vs. Job Median

**Logic:** Compare the customer's credit amount to the typical (median) credit taken by others with the same job type.

- 📈 If it's **significantly higher** → **+1 risk** (Borrowing above means possible over-leverage)  
- 📉 If it's **much lower** → **-1 risk** (More conservative borrower)

---

### 💼 2. Job Category

**Logic:** Job type indicates income stability.

- 🧑‍🏭 **Unskilled** → **+1 risk** (Less stable income)  
- 👷 **Skilled** → No change (Neutral)  
- 👨‍💼 **Highly Skilled/Managerial** → **-1 risk** (Stable and higher income)

---

### 🏦 3. Checking Account Balance

**Logic:** Shows short-term liquidity.

- 💸 **No account or very low balance** → **+1 risk**  
- 💵 **High balance** → **-1 risk**  
- ❓ **Missing data** → Treat as risky → **+1 risk**

---

### 💾 4. Saving Account Status

**Logic:** Indicates long-term financial planning.

- 🚫 **No savings / little** → **+1 risk**  
- 🟡 **Moderate savings** → No effect  
- 🟢 **Good / Rich savings** → **-1 risk**

---

### ⏳ 5. Duration of Loan

**Logic:** Longer repayment period = higher chance of default.

- 📆 **> 48 months** → **+1 risk**  
- 📉 **< 12 months** → **-1 risk**

---

### 🏠 6. Housing Status

**Logic:** Asset ownership adds to financial reliability.

- 🏘️ **Renting** → **+1 risk** (More monthly obligations)  
- 🏡 **Own house** → **-1 risk** (Asset ownership = financial stability)  
- 🆓 **Free housing** → Neutral

---

## 🚨 Final Risk Flag Logic

After calculating the total `risk_score`:

- If **risk_score > 1** → Flagged as **Risky (`CreditRisk = 1`)** 🚩  
- Else → Considered **Safe (`CreditRisk = 0`)** ✅

---

### 🧠 Example:

| Feature              | Value              | Risk Impact |
|----------------------|--------------------|-------------|
| Credit Amount        | High for job type  | +1          |
| Job                  | Unskilled          | +1          |
| Checking Account     | None               | +1          |
| Saving Account       | Moderate           | 0           |
| Duration             | 60 months          | +1          |
| Housing              | Own                | -1          |
| **Total Risk Score** |                    | **+3**       |

**➡️ Result:** Risky Customer (`CreditRisk = 1`) 🚩



## 🔍 Model Insights

✅ **Best Model:** Gradient Boosting Classifier  
📈 **ROC AUC Score:** `0.99`  
📋 **Accuracy:** `96%`  
📊 **Confusion Matrix:**  
```
[[177   4]
 [  8 111]]
```

### ⭐ Top 5 Important Features:
1. Credit amount
2. Housing
3. Job
4. Checking account
5. Saving accounts

---

## 💡 Recommendations

- Flag customers with **high credit amounts** or **long loan durations**.
- Automate initial risk scoring to **speed up approvals**.
- **Retrain model quarterly** to adjust for changing trends.
- Use risk score to **tailor interest rates** or **collateral requirements**.

---

## 📁 Project Structure

- `app.py` → Streamlit app  
- `credit_risk_pipeline.pkl` → Trained ML pipeline  
- `encoders.pkl` → Label encoders for categorical features  
- `requirements.txt` → Python libraries list

---

## 🛠️ Installation

1. Clone the repo  
2. Install dependencies  
3. Run the app!

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🙌 Acknowledgements

- Dataset by **UCI Machine Learning Repository**
- Inspired by **real-world credit risk scoring systems**

