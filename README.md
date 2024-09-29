# Movie Recommendation System

This project is a movie recommendation system that provides users with new movie suggestions based on the movies they have previously watched. It uses content-based filtering and collaborative filtering techniques to make recommendations.

## Features

- **Display the movies watched by the user:**  
  Users can view a list of movies they have previously watched.

- **Provide personalized movie recommendations:**  
  Based on the movies users have watched, the system provides new movie recommendations that match their interests.

- **Simple web interface with Streamlit:**  
  The application features an easy-to-use web interface built with Streamlit.

## Technologies Used

- **Python**: For data analysis and building machine learning models.
- **Pandas**: For data processing and analysis.
- **Surprise**: For building the collaborative filtering model for movie recommendations.
- **Scikit-learn**: For content-based filtering (TF-IDF and cosine similarity).
- **Streamlit**: For creating a web interface for users to interact with the recommendation system.

## Installation and Running

### Requirements

- **Python 3.7+**
- **Pip or Conda package manager**

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Bbakac/movie-recommendation-system.git
   cd movie-recommendation-system

## Installation and Running

### Requirements

- **Python 3.7+**
- **Pip or Conda package manager**

### Steps

2. **Prepare the Dataset**  
   Place the `movie.csv` and `rating.csv` files in the `/data` directory. These files contain user ratings and movie information.

3. **Run the Application**  
   To start the Streamlit application, use the following command:

   ```bash
   streamlit run filmApp.py

### View in Browser

After starting the application, copy the `Local URL` provided in the terminal to your browser to view the app (usually `http://localhost:8501`).

## Usage

- **Enter User ID:**  
  Enter a user ID to view the movies you have previously watched and get personalized recommendations.

- **Recommendations:**  
  Based on the entered ID, the watched movies and the recommended movies will be listed.

## Project Structure

- **`filmApp.py`**  
  The file that runs the Streamlit-based web application.

- **`data/`**  
  Directory where `movie.csv` and `rating.csv` files are located.
