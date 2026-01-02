<h1 align="center">🏏 IPL First Innings Score Prediction</h1>

<p align="center">
  🚀 End-to-End Machine Learning Web Application  
  <br>
  📊 Built as part of an <b>InternPe Machine Learning Internship Task</b>
</p>

<hr>

<h2>📌 Project Overview</h2>
<p>
This project is an <b>end-to-end Machine Learning web application</b> that predicts the
<b>final first-innings score in IPL matches</b> based on real-time match conditions.
</p>

<p>
A <b>Random Forest Regression</b> model is trained on historical IPL ball-by-ball data
and deployed using <b>Flask</b>, with a clean frontend interface for user interaction.
</p>

<hr>

<h2>✨ Key Features</h2>
<ul>
  <li>🏏 Predicts IPL first-innings final score</li>
  <li>📈 Uses live match context:
    <ul>
      <li>Batting team & bowling team</li>
      <li>Current runs and wickets</li>
      <li>Overs completed</li>
      <li>Runs & wickets in last 5 overs</li>
    </ul>
  </li>
  <li>🧠 End-to-end ML workflow (training → deployment)</li>
  <li>🌐 Interactive web interface</li>
</ul>

<hr>

<h2>🧠 Machine Learning Details</h2>
<ul>
  <li><b>Dataset:</b> IPL ball-by-ball match data</li>
  <li><b>Model:</b> Random Forest Regressor</li>
  <li><b>Libraries:</b> Scikit-learn, Pandas, NumPy</li>
  <li><b>Model Selection:</b> Multiple models evaluated, Random Forest selected</li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>🐍 Python</li>
  <li>📊 Machine Learning (Scikit-learn)</li>
  <li>🌐 Flask (Backend)</li>
  <li>🎨 HTML, CSS, JavaScript (Frontend)</li>
  <li>💾 Joblib (Model Serialization)</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>
<pre>
ipl-win-predictor/
│
├── app.py
├── forest_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── data.csv
</pre>

<hr>

<h2>▶️ How to Run</h2>
<ol>
  <li>Clone the repository</li>
  <li>Install required dependencies</li>
  <li>Run the Flask app using <code>python app.py</code></li>
  <li>Open <code>http://127.0.0.1:5000</code> in your browser</li>
</ol>

<hr>

<h2>🚀 Future Enhancements</h2>
<ul>
  <li>📉 Add win probability prediction</li>
  <li>📊 Improve accuracy with advanced feature engineering</li>
  <li>☁️ Deploy on cloud platforms (Render / Heroku)</li>
  <li>🎨 Enhance UI and user experience</li>
</ul>

<hr>

<h2>🙌 Acknowledgements</h2>
<p>
This project was developed as part of a <b>Machine Learning internship task provided by InternPe</b>.
</p>

<hr>

<p align="center">
  ⭐ If you like this project, consider starring the repository!
  <br>
  🤝 Open to feedback and collaboration
</p>
