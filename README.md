# NF Mortality Calculator

This public repository contains the standalone NF mortality calculator app. Open the [hosted calculator](https://jpg123.github.io/NF-mortality-calculator/) or open `index.html` locally. Calculations run in the browser; entered values are not sent to a server. Do not enter identifiable patient information into shared messages or screenshots.

## Included

- `index.html`: canonical app and embedded coefficient implementation
- `data/study_data.json`: companion model metadata and coefficient audit file; the browser calculation uses the coefficient inventory embedded in `index.html`
- `App_Explainer.html`: user-facing explanation of the app outputs
- `manifest.json`, `icon.svg` and `sw.js`: installable-app metadata and offline support

This is the app code only. It does not include patient-level records, analysis datasets or the model-development pipeline.

## Calculation and intended use

The calculator displays the estimated in-hospital mortality probability from its coefficient-based logistic-regression implementation:

`risk = 1 / (1 + exp(-linear predictor))`

The linear predictor combines the fitted intercept and transformed input contributions. Blank laboratory values are omitted from the app calculation. Component contributions are descriptive parts of the implemented calculation, not causal effects.

Risk categories are descriptive probability bands: below 15%, 15% to less than 50%, and 50% or above. These bands are not validated clinical decision thresholds. This research and education app is intended for the study population described in the companion manuscript. It is not a substitute for clinical assessment or local protocols. The model has not undergone external validation or prospective clinical evaluation.

App source and coefficient files were reviewed on October 23, 2026. The review date does not indicate that the coefficients were newly fitted or clinically validated; see the dated submission audit for the unresolved analysis-to-app reproducibility issue. The calculator uses each `weight` value; the JSON `or` fields are not read by the app. The blood product receipt record has `or: 0.81`, while the exponential of its app coefficient (-0.168593) is approximately 0.85; the source of this unused OR metadata remains to be verified.


## License

This app is licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE) for the terms.
