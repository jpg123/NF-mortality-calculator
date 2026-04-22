# NF Mortality Predictor (Peer Review Repository)

**Prognostic Support for Necrotizing Fasciitis at the Point of Admission**

---

## Abstract
**Background:** Accurate mortality risk assessment in necrotizing fasciitis (NF) is critical for triage and resource allocation. Traditional clinical scores often lack prognostic precision at admission. This study developed an interpretable machine learning (ML) framework for predicting in-hospital mortality using admission-only clinical indicators.

**Methods:** A point-of-care mobile application was created based on the analysis of a 21-year retrospective Canadian provincial registry (2004–2024) of 565 adult patients. Missing values were handled using MICE. Confounding was addressed via standardized IPTW weighting. Explainable AI (SHAP) and weighted logistic regression were used to identify risk drivers.

**Results:** Overall mortality was 14.0%. An extreme gradient boosting (XGBoost) model demonstrated high discrimination (AUC: 0.853), prognostic specificity (99.0%), and PPV (83.3%). Key independent predictors included synchronous multifocal involvement (AOR 8.40), ICU admission (AOR 5.81), and renal disease (AOR 2.63).

**Conclusions:** Machine learning provides robust, transparent mortality prediction in NF. Integrating these models into clinical workflows via digital decision supports can improve surgical triage and prognostic discussions.

---

## Methodology
The prognostic framework utilizes an **XGBoost** architecture validated on a whole-population registry from Manitoba, Canada (2004–2024). This mobile application was developed to directly implement these machine learning outputs and predictive logic for point-of-care utility.
- **Preprocessing:** Missing laboratory values were handled using Multiple Imputation by Chained Equations (MICE). Confounding was addressed via standardized Inverse Probability of Treatment Weighting (IPTW; mortality exposure) using restricted cubic splines for age.
- **Architecture:** The model focuses exclusively on admission-only clinical and laboratory predictors, excluding intraoperative variables to ensure point-of-care utility. Model performance was validated via a randomized 80/20 train-test split (Test set n=113).
- **Interpretability:** Local interpretability is established via SHapley Additive exPlanations (SHAP), providing a visual decomposition of patient-specific risk drivers at the bedside.
- **Missing Data Handling (Point-of-Care Fallbacks):** To ensure utility in environments where complete laboratory data may not yet be available, the application allows for missing inputs. If a lab value is not provided, the engine assumes a "baseline" (normal) value (e.g., WBC 15.0, Urea 5.0, Albumin 35) and alerts the user before calculating.

---

## Validation
The model demonstrates high prognostic reliability compared to traditional linear scoring systems:
- **Discrimination:** AUC of **0.853** (XGBoost).
- **Prognostic Reliability:** Specificity of **99.0%** and PPV of **83.3%** at the classified threshold.
- **Primary Drivers:** SHAP analysis and weighted multivariate models identified **synchronous multifocal involvement** (OR 8.40), **ICU admission** (OR 5.81), and **renal insufficiency** (OR 2.63) as the primary independent mortality drivers.

---

## Installation & Deployment
This tool is built using a mobile-first HTML5/JavaScript architecture, requiring no backend server.

### 1. Local Deployment
To run the predictive dashboard locally:
1. Clone this repository.
2. Open `index.html` in any modern web browser.
3. No dependencies or `pip install` required for the dashboard itself.
4. Use `NF_Mortality_Predictor.html` as the app file when sharing the tool.

### 2. PWA Installation (Mobile Device)
The application is a Progressive Web App (PWA):
- **iOS:** Open in Safari → Share → "Add to Home Screen".
- **Android:** Open in Chrome → Three Dots → "Install App".

---

## Clinical Research Disclaimer
This predictive tool is intended for research and educational purposes only. It is not a medical device and has not been cleared for clinical use by Health Canada or the FDA. The predictions generated are based on retrospective analysis and should not be used to direct individual patient care or replace professional clinical assessment.

---

## Features
- **Admission-Time Prediction:** Near-instant risk stratification using admission variables.
- **SHAP Visualization:** Near-instant visual feedback on patient-specific risk drivers.
- **Offline Capable:** Full PWA support for use in low-connectivity clinical environments.

---

## 📅 Version Info
- **Last Updated:** April 20, 2026
- **Version:** 2026-04-20 14:14
- **License:** [Apache License, Version 2.0](LICENSE)

## 📚 References
1. **Marschner IC, Gillett AC.** Relative risk regression: reliable sandwich covariance estimators for independent observations. *Stat Med.* 2017;36(19):3048-3063.
2. **Huber J.** necrotizing_fasciitis: Open-source machine learning framework for necrotizing fasciitis mortality. GitHub Repository. 2024.

## ✉️ Questions?
If you have questions about the logic, the study, or the application, please contact:
**[Support](mailto:logsetty@umanitoba.ca?subject=NF%20mortality%20predictor)**

 ---
