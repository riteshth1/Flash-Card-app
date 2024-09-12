<h1>Flash Card App</h1>

<p>This is a simple Flash Card application built with Python's <code>tkinter</code> library. The app helps users learn new words by flipping cards with French words on the front and their English translations on the back. Users can mark words they already know, and the app will remove them from the list of words to learn.</p>

<h2>Features</h2>

<ul>
  <li><strong>Flashcards for learning French to English</strong>: Displays a random French word and its English translation after 3 seconds.</li>
  <li><strong>Track words you know</strong>: Once a word is marked as "known", it is removed from the learning pool and saved to a file.</li>
  <li><strong>Save progress</strong>: Words that are marked as "known" are saved, allowing you to continue learning where you left off.</li>
</ul>

<h2>How It Works</h2>

<ol>
  <li>The app initially reads from a CSV file (<code>french_words.csv</code>) containing a list of French-English word pairs.</li>
  <li>When a word is marked as known by clicking the right button, it is removed from the word pool and saved to another CSV file (<code>words_to_learn.csv</code>).</li>
  <li>The app automatically flips the card to show the English translation after 3 seconds.</li>
  <li>You can cycle through the words using the wrong button to see the next card.</li>
</ol>

<h2>Installation</h2>

<h3>Prerequisites</h3>

<ul>
  <li>Python 3.x</li>
  <li><code>tkinter</code> library (comes pre-installed with Python on most systems)</li>
  <li><code>pandas</code> library (for reading/writing CSV files)</li>
</ul>

<h3>Clone the Repository</h3>

<pre><code>git clone https://github.com/riteshth1/Flash-Card-app.git
cd flash-card-app
</code></pre>

<h3>Install Dependencies</h3>

<p>You will need to install the required libraries. Use the following command to install pandas:</p>

<pre><code>pip install pandas
</code></pre>

<h3>Directory Structure</h3>

<p>Ensure that your directory has the following structure:</p>

<pre><code>
flash-card-app/
│
├── data/
│   ├── french_words.csv        # The original list of French words
│   └── words_to_learn.csv      # Automatically generated after you start marking known words
│
├── images/
│   ├── card_front.png          # Image for the front of the flashcard
│   ├── card_back.png           # Image for the back of the flashcard
│   ├── right.png               # Image for the 'right' button
│   └── wrong.png               # Image for the 'wrong' button
│
└── flash_card_app.py           # The main Python script
</code></pre>

<h3>Running the App</h3>

<p>To start the Flash Card App, run the following command:</p>

<pre><code>python flash_card_app.py
</code></pre>

<h2>Usage</h2>

<ul>
  <li>The app will show a French word.</li>
  <li>After 3 seconds, the card will automatically flip and display the English translation.</li>
  <li>If you know the word, click the <strong>Right button</strong> (✔️), and the word will be removed from your learning pool.</li>
  <li>If you don't know the word, click the <strong>Wrong button</strong> (❌), and the app will show another word without removing it from the list.</li>
</ul>

<h2>Screenshots</h2>

<p><img src="images/card_front.png" alt="Flash Card App" width="400"></p>
<p><em>Front of the flashcard displaying a French word.</em></p>

<h2>Customizing the Data</h2>

<p>You can customize the app by providing your own CSV files with different words to learn. The CSV file must have the following columns:</p>

<pre><code>French,English
</code></pre>

<h2>Dependencies</h2>

<ul>
  <li>Python 3.x</li>
  <li><code>tkinter</code> for the GUI</li>
  <li><code>pandas</code> for handling CSV files</li>
</ul>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
