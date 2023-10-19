# Import necessary libraries and modules
from serpapi import GoogleSearch
import pandas as pd
import time
import unique_algorithm
from posterFind import posterPathFind

# Define a function to perform spelling correction using Google search
def Spell_fix(input):
    # Define search parameters
    params = {
        "q": input + " movie",
        "hl": "en",
        "gl": "us",
        "api_key": "b48b64bd362615156557823cf6ac5795c248c4c384c84edf1d73bd1aca3eba32"
    }
    # Create a Google search object
    search = GoogleSearch(params)
    # Get search results as a dictionary
    results = search.get_dict()
    # Extract spelling correction information
    search_information = results["search_information"]
    spelling_fix = search_information.get("spelling_fix")
    
    # Check if there is a spelling fix available
    if spelling_fix is not None:
        # Process and extract corrected keywords
        spelling_fix = spelling_fix.replace(" movie", '')
        spelling_fix = spelling_fix.strip().split()
    else:
        # If no correction is found, split the original input
        input = input.split()
        return input
    
    # Print and return the corrected keywords
    print(spelling_fix)
    return spelling_fix

# Define a function to process data from a CSV file
def data_process():
    # Read data from a CSV file
    df = pd.read_csv('movie_preprocessing.csv', low_memory=False)
    
    # Define a function to replace spaces with underscores in specific columns
    def change_value(value):
        return str(value).replace(' ', '_')

    # Apply the column value transformation to specific columns
    df['genres'] = df['genres'].apply(change_value)
    df['original_language'] = df['original_language'].apply(change_value)
    df['production_companies'] = df['production_companies'].apply(change_value)
    df['production_countries'] = df['production_countries'].apply(change_value)
    df['belongs_to_collection'] = df['belongs_to_collection'].apply(change_value)

    return df

# Define a function to extract tags and keywords from an input string
def extract_tags_and_keywords(input_string):
    tags = []
    keywords = []

    # Split the input string into words
    words = input_string.split()

    # Extract tags and keywords
    for word in words:
        if word.startswith('+'):
            tags.append(word[1:])
        elif not word.startswith('('):
            keywords.append(word)
    return [tags, keywords]

# Define a function to search for movies by title
def title_search(dataframe, keyword):
    keyword = "|".join(keyword)
    filtered_df = dataframe[dataframe['title'].str.contains(keyword, case=False, na=False) |
                          dataframe['original_title'].str.contains(keyword, case=False, na=False) |
                          dataframe['keywords'].str.contains(keyword, case=False, na=False)]
    return filtered_df

# Define a function to filter data based on tags
def tag_search(dataframe, tags, genres_tags, language_tags, production_countries_tags, collection_tags, production_companies_tags):
    if len(tags) == 0:
        return dataframe
    for tag in tags:
        tag = tag.lower()
        if tag == "+adult":
            dataframe = dataframe[dataframe['adult'].str.contains("TRUE", case=False, na=False)]
        elif tag in genres_tags:
            dataframe = dataframe[dataframe['genres'].str.contains(tag, case=False, na=False)]
        elif tag in language_tags:
            dataframe = dataframe[dataframe['original_language'].str.contains(tag, case=False, na=False)]
        elif tag in production_countries_tags:
            dataframe = dataframe[dataframe['production_countries'].str.contains(tag, case=False, na=False)]
        elif tag in production_companies_tags:
            dataframe = dataframe[dataframe['production_companies'].str.contains(tag, case=False, na=False)]
        elif tag in collection_tags:
            dataframe = dataframe[dataframe['belongs_to_collection'].str.contains(tag, case=False, na=False)]
            print("true")
        else:
            return pd.DataFrame(columns=dataframe.columns)
    return dataframe

# Define a function to filter and process movie data based on user input
def DataFilter(User_input, spell_check=True):
    # Process the data from a CSV file
    df = data_process()
    genres_tags = unique_algorithm.unique_genres_read
    language_tags = unique_algorithm.unique_language_read
    production_companies_tags = unique_algorithm.unique_production_companies_read
    production_countries_tags = unique_algorithm.unique_production_countries_read
    collection_tags = unique_algorithm.unique_belongs_to_collection_read
    print(collection_tags)

    # Extract keywords and tags from user input
    keyword = extract_tags_and_keywords(User_input)[1]
    
    # Perform spelling correction if enabled
    if spell_check:
        corrected_keyword = Spell_fix(" ".join(keyword))
        keyword_output = " ".join(corrected_keyword)
        if corrected_keyword != keyword:
            print(f"Showing result for {keyword_output}")
        keyword = corrected_keyword
    
    tags = extract_tags_and_keywords(User_input)[0]
    
    # Search for movies by title and filter based on tags
    Movie_list = title_search(df, keyword)
    Movie_list = tag_search(Movie_list, tags, genres_tags, language_tags, production_countries_tags, collection_tags, production_companies_tags)
    
    # Add a 'poster_path' column to the DataFrame using posterPathFind
    Movie_list['poster_path'] = Movie_list['imdb_id'].apply(posterPathFind)
    
    return [Movie_list, corrected_keyword]

# Example usage and timing of the DataFilter function
# start_time = time.time()
# result = DataFilter("+mark_collection")
# print(result[0])
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")
