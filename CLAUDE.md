# Data Science HW2 - Error Analysis Project Guidelines

## Project Context
- **Course:** Introduction to Data Science (Regression and Classification Error Analysis)
- **Dataset:** Used Cars (craigslist-carstrucks)
- **Main Tool:** Jupyter Notebook (`.ipynb`)
- **Primary Languages:** Python (Code), English (Documentation/Markdown)

## Coding Standards & Style
- **No Generic Names:** NEVER use generic variable names like `df`, `data`, `temp`, `x`, or `y` in the final code. Use highly descriptive names (e.g., `used_cars_raw`, `X_train_scaled`, `rf_predictions`, `residuals_xgb`).
- **Modularity:** Keep notebook cells focused on a single logical task (e.g., data loading, specific plot, single model training).
- **Execution Consistency:** Always ensure notebooks can execute cleanly from top to bottom (`Clear All Outputs` -> `Restart & Run All`) without hidden state dependencies.
- **Visualizations:** Use `seaborn` and `matplotlib`. Every plot MUST have a clear title, x-label, and y-label.

## Git & GitHub Workflow Automation
- Before committing, silently analyze the exact changes made to ensure everything is correct.
- Write clear, conventional commit messages summarizing the technical changes (e.g., "feat: add XGBoost model and residual plots").
- **Auto-Push:** After a successful commit, automatically push the changes to the remote repository. Do not wait for explicit user permission if the commit was successful.

## Assignment Specific Rules (HW2)
- Ensure exact alignment with the HW2 rubric: K-fold cross-validation is mandatory.
- Clearly separate Part 1 (Regression Error Analysis), Part 2 (Regression Models), and Part 3 (Classification Models & Error Analysis).