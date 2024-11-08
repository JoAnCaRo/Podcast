# 🎙️ Podcast Recommendation Platform

A terminal-based Python application that helps users discover podcasts based on **name**, **theme**, or **rating**. This project demonstrates how to implement a recommendation system using Python.

## 📋 Table of Contents
- [🎙️ Podcast Recommendation Platform](#️-podcast-recommendation-platform)
  - [📋 Table of Contents](#-table-of-contents)
  - [📝 About](#-about)
  - [✨ Features](#-features)
  - [🚀 How to Run](#-how-to-run)
    - [Prerequisites](#prerequisites)
    - [Running the Project](#running-the-project)
  - [🖱️ Instructions](#️-instructions)
    - [Example Commands:](#example-commands)
  - [📂 Project Structure](#-project-structure)
  - [🔍 Example Output](#-example-output)
  - [🛠️ Technologies Used](#️-technologies-used)
  - [🤝 Contributions](#-contributions)
    - [How to Contribute](#how-to-contribute)
  - [📄 License](#-license)
  - [🙌 Acknowledgements](#-acknowledgements)

## 📝 About
The Podcast Recommendation Platform allows users to search and discover podcasts using different filters:
- Search by **name**: Enter the starting letters of a podcast name.
- Search by **theme**: Choose from various podcast categories like `Culture`, `Technology`, `History`, etc.
- Search by **rating**: Filter podcasts based on user ratings from 1 to 5.

## ✨ Features
- **User-friendly terminal interface** for selecting podcasts.
- Supports filtering by **name**, **theme**, or **rating**.
- Provides detailed information on selected podcasts, including category, seasons, rating, and description.
- Easily extendable to include new search criteria or podcast data.

## 🚀 How to Run

### Prerequisites
Make sure you have Python installed on your system:
```bash
python3 --version
```

### Running the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/JoAnCaRo/Podcast.git
   cd Podcast
   ```
2. Ensure you have the required data file `podcast_data.py` in the same directory.
3. Run the program:
   ```bash
   python3 Podcast.py
   ```

## 🖱️ Instructions
Here’s how you can use the platform:
1. **Select a search option**:
   - `n`: Search by **name**.
   - `t`: Search by **theme**.
   - `v`: Search by **rating**.
2. Follow the prompts to find podcasts that match your search criteria.

### Example Commands:
- Enter `n` to search for podcasts by name.
- Enter `t` to search by theme. You'll be prompted to select from available themes like `Technology`, `Culture`, etc.
- Enter `v` to search by rating (1-5).

## 📂 Project Structure
```
Podcast/
│
├── script.py                # Main Python script
├── podcast_data.py          # Data file with podcast information
└── README.md                # Project documentation
```

## 🔍 Example Output
After running the program, here’s an example of what you might see:
```
##############################################
WELCOME TO THE PODCAST RECOMMENDATION PLATFORM!
##############################################

Select 'n' if you want to choose your podcast by NAME.
Select 't' if you want to choose your podcast by THEME.
Select 'v' if you want to choose your podcast by RATING.

Enter your choice: t

Select a theme:
'a' for Astronomy
'c' for Culture
'te' for Technology

You selected Technology:
Podcast found: TECH INSIDER
- Seasons: 5
- Rating: 4/5
- Description: A deep dive into the latest in tech.
```

## 🛠️ Technologies Used
- **Python 3.x**

## 🤝 Contributions
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository, make changes, and submit a pull request.

### How to Contribute
1. Fork the project.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## 📄 License
This project is open-source and available under the MIT License.

## 🙌 Acknowledgements
Special thanks to everyone who has supported this project!

Happy podcast discovering! 🎧🚀
