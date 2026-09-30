# Project Statement: Student Expense Tracker

## Problem Statement
College students frequently struggle with financial management due to limited income, irregular expenses, and a lack of budgeting experience. Existing corporate expense tools are overly complex, feature-heavy, and often require paid subscriptions. 

Without a clear, localized, and simple mechanism to log daily spending, students often face **unexpected cash shortages, accidental overspending, and financial stress** before the end of the academic term. There is a distinct need for a lightweight, intuitive, and immediate tracking system tailored to standard student spending behaviors.

---

## Scope of the Project
The project covers the development of a lightweight financial tracking utility focused on immediate user feedback and minimal data entry friction.

### In-Scope
* **Core Ledger Systems:** Interactive entry mechanisms for recording amounts, specific dates, and categories.
* **Predefined Categorisation:** Localised grouping optimized for student life (e.g., Food, Books, Transport, Rent, Entertainment).
* **Dynamic Analytics:** Real-time generation of percentage breakdowns and visual time-frame filtering (7 days, 30 days, All-time).
* **Budget Enforcement:** Active checking against a user-defined threshold with automated visual warnings upon violation.

### Out-of-Scope
* **Multi-user Sync:** Cloud database hosting, user registration, and cross-device account syncing.
* **Open Banking API:** Direct linking to real bank accounts, UPI apps, or credit card SMS scrapers.
* **Predictive AI:** Machine learning algorithms to forecast future spending patterns.

---

## Target Users
The system is explicitly engineered for individuals navigating academic and limited-budget environments:
* **Hostel & Dorm Residents:** Students managing independent living expenses like rent, utilities, and mess bills for the first time.
* **Commuter Students:** Users tracking high-frequency daily micro-transactions such as public transport fares and quick meals.
* **Scholarship / Stipend Recipients:** Individuals who receive fixed monthly or quarterly payouts and must strictly pace their distributions to avoid deficits.

---

##  High-Level Features

* **Instant Transaction Logging**
  * One-click categorization with validation checks to block invalid or negative currency figures.
  * Automatic timestamps applied to each entry to accurately monitor spending history.

* **Dynamic Timeframe Filtering**
  * On-demand generation of **Weekly (Last 7 Days)** snapshots to evaluate short-term micro-habits.
  * On-demand generation of **Monthly (Last 30 Days)** summaries to measure recurring utility and billing cycles.

* **Visual Analytics Engine**
  * Automatic calculation of category-wise ratios against total expenditure.
  * Clean, tabular distribution formatting presenting exact figures and relative percentages side-by-side.

* **Proactive Budget Guardrails**
  * Customizable global budget caps with the ability to completely disable thresholds by scaling to zero (`0`).
  * Real-time calculation alerts executed immediately before transaction confirmation to prevent catastrophic account over-drafting.
