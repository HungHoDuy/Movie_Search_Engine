from nicegui import ui
import pandas as pd

# Load the dataset
dataset_path = 'data/movies_metadata.csv'
movies_df = pd.read_csv(dataset_path, low_memory=False)

# Input for entering keywords
keywords_input = ui.input('Enter keywords')

# Labels and select elements for choosing genres and languages
ui.label('Select Genre')
genre_select = ui.select(options=['Action', 'Comedy', 'Drama', 'Horror'])
ui.label('Select Language')
language_select = ui.select(options=['English', 'Spanish', 'French', 'German'])

# Labels and sliders for selecting runtime, release year, and user rating
ui.label('Select Runtime')
runtime_slider = ui.slider(min=0, max=300, step=10)
ui.label('Select Release Year')
year_slider = ui.slider(min=1900, max=2023, step=1)
ui.label('Select User Rating')
rating_slider = ui.slider(min=0, max=10, step=0.1)

# Creating a new row to display the search results
results_row = ui.row()

# Function to execute the search based on the selected criteria
def execute_search():
    keywords = keywords_input.value
    genre = genre_select.value
    language = language_select.value
    runtime = runtime_slider.value
    year = year_slider.value
    rating = rating_slider.value

    # Simple filter based on the movie title for now
    results = movies_df[movies_df['title'].str.contains(keywords, case=False, na=False)]

    # Display the results in the results row
    display_results(results)

# Function to display results in the results row
def display_results(results):
    # Clear previous results
    results_row.clear()

    # Create a table to display the results
    columns = [{'name': 'title', 'label': 'Title'}]  # You can add more columns as needed
    rows = results[['title']].to_dict(orient='records')  # Convert DataFrame to a list of dicts
    results_table = ui.table(columns=columns, rows=rows, on_row_click=show_details)

    # Add the results table to the results row directly
    results_row <= results_table

# Function to show details of the selected movie
def show_details(row):
    movie = movies_df.iloc[row]
    ui.notify(f"Title: {movie['title']}\nGenre: {movie['genres']}\nOverview: {movie['overview']}")

# Search button to execute the search based on the selected criteria
ui.button('Search', on_click=execute_search)

# Running the NiceGUI app
ui.run()
