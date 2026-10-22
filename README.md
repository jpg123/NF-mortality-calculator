# NF Mortality Calculator

This repository contains the standalone NF mortality calculator app. Open `index.html` in a browser. The app runs locally; its calculations do not send entered values to a server. Do not enter identifiable patient information into shared messages or screenshots.

## Included

- `index.html`: canonical app and embedded coefficient implementation
- `data/study_data.json`: app model metadata and explanatory values
- `App_Explainer.html`: user-facing explanation of the app outputs
- `manifest.json`, `icon.svg` and `sw.js`: installable-app metadata and offline support

This is the app code only. It does not include patient-level records, analysis datasets or the model-development pipeline.

## Calculation and intended use

The calculator displays the estimated in-hospital mortality probability from its coefficient-based logistic-regression implementation:

`risk = 1 / (1 + exp(-linear predictor))`

The linear predictor combines the fitted intercept and transformed input contributions. Blank laboratory values are omitted from the app calculation. Component contributions are descriptive parts of the implemented calculation, not causal effects.

This research and education app is intended for the study population described in the companion manuscript. It is not a substitute for clinical assessment or local protocols. The model has not undergone external validation or prospective clinical evaluation.


## License

No reuse license is included. Contact the study team before adapting or redistributing this code.
