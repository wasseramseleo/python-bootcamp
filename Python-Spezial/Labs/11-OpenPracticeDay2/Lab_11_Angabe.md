# Lab 11: Open Practice (Tag 2)

### Szenario

Sie haben nun Zugriff auf das volle Arsenal der Python Data Science Tools. In dieser Session vertiefen wir spezifische Aspekte, die für Finanzanalysen kritisch sind: Zeitreihen-Glättung, hierarchische Visualisierung und binäre Klassifikation (Betrugserkennung).

**Freie Aufgabenwahl.**


-----

### Option A: Pandas (Advanced Time Series)

Analysten schauen selten auf tagesaktuelle, volatile Zahlen. Sie wollen Trends sehen.

**Aufgabe:**

1.  Laden Sie die Daten und setzen Sie das Datum als Index.
2.  **Daily Aggregation:** Berechnen Sie das tägliche Gesamtvolumen (`sum` von `amount`).
3.  **Rolling Window:** Erstellen Sie eine neue Spalte `7d_moving_avg`.
      * Berechnen Sie den gleitenden Durchschnitt der letzten 7 Tage über das tägliche Volumen.
      * Nutzen Sie dazu `.rolling(window=7).mean()`.
4.  **Volatility:** Berechnen Sie die prozentuale Veränderung zum Vortag (`pct_change()`) für das tägliche Volumen.

-----

### Option B: Plotly (Hierarchische Charts)

Bankmanager wollen sehen, wie sich das Kapital verteilt ("Asset Allocation"), aufgebrochen nach Region und Anlageklasse. Balkendiagramme sind hierfür oft unübersichtlich.

**Aufgabe:**

1.  Laden Sie die Daten.
2.  **Sunburst Chart:** Nutzen Sie `px.sunburst`, um die Hierarchie darzustellen.
      * **Ebene 1 (Innen):** `customer_region`
      * **Ebene 2 (Außen):** `asset_class`
      * **Größe der Segmente:** `amount`
3.  **Interaktivität:** Fahren Sie mit der Maus über die Segmente, um zu prüfen, ob die Summen korrekt aggregiert werden.
4.  **Titel:** Setzen Sie einen passenden Titel, z.B. "Global Asset Allocation".

-----

### Option C: Scikit-learn (Fraud Detection / Classification)

In Lab 09 haben wir Werte vorhergesagt (Regression). Nun wollen wir Kategorien vorhersagen (Klassifikation): Ist eine Transaktion Betrug (1) oder nicht (0)?

**Aufgabe:**

1.  **Feature Prep:**
      * Nutzen Sie `amount` als Feature.
      * Erstellen Sie ein Dummy-Feature für `asset_class` (Text muss in Zahlen gewandelt werden). Nutzen Sie dazu `pd.get_dummies()`.
      * Target (`y`) ist die Spalte `is_fraud`.
2.  **Split:** Teilen Sie in Train/Test (70%/30%).
3.  **Model:** Importieren Sie `LogisticRegression` aus `sklearn.linear_model` (der Standard für binäre Klassifikation im Banking). Trainieren Sie das Modell.
4.  **Evaluation (Confusion Matrix):**
      * Ein R²-Score ergibt bei Klassifikation keinen Sinn. Wir brauchen eine "Confusion Matrix".
      * Importieren Sie `confusion_matrix` und `ConfusionMatrixDisplay` aus `sklearn.metrics`.
      * Vergleichen Sie die Vorhersagen (`y_pred`) mit den echten Werten (`y_test`) und zeigen Sie die Matrix an oder geben Sie sie als Text aus.
      * *Frage:* Wie viele Betrugsfälle (True Positives) wurden korrekt erkannt?
