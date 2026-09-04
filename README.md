# NF Mortality Calculator

## How to use the app

1. Open the deployed calculator in a mobile or desktop browser.
2. Review the research-use disclaimer.
3. Select the available patient characteristics, clinical findings and laboratory values.
4. Select **Calculate risk**.
5. Review the estimated in-hospital mortality percentage, risk category and model-component contributions.
6. Use **Reset** to enter another patient.
7. Use **Share App** to send the public calculator link through Messages, iMessage or another sharing service. The link does not include patient information.

The calculator is intended for research, education and discussion. It does not replace surgical assessment, consultation with an appropriate clinical team or local protocols. Do not enter identifiable patient information into a shared link or message.

## Technical information

The app is a standalone static calculator. The validated NF model intercept, weights, preprocessing rules and thresholds are embedded in `index.html` so the deployed URL can be opened and shared without a separate model download. `data/study_data.json` is retained as the source/audit representation of the model artifact.

The estimate is produced by the fitted logistic model:

`risk = 1 / (1 + exp(-linear predictor))`

The linear predictor is the intercept plus the contribution of every entered covariate. Continuous variables and threshold indicators use the model-defined transformations. Component contributions describe the implemented coefficient calculation; they are not SHAP or LIME explanations and should not be interpreted as causal effects.

The model is intended for the study population and internal-validation context described in the accompanying manuscript. External validation and prospective clinical evaluation remain separate requirements.

## Shared analysis pathway

The NF and burn mortality papers should use a similar analysis pathway where appropriate: prespecified covariates; explicit coding and clinically justified binning; leakage-resistant fold-local preprocessing; stratified internal validation; comparison with a simple logistic baseline and other candidate models; L2-penalized multivariable logistic regression when supported by the finalized analysis; calibration and discrimination reporting; and transparent documentation of the model used by the app. The covariates, coefficients, cohort definitions and clinical interpretations remain study-specific and must not be copied between studies.
