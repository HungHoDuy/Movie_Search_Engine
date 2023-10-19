import streamlit as st
from relevant import relevant_df
from unique import unique_genres, unique_language, unique_production_companies, unique_belongs_to_collection, unique_production_countries

# Preconf
st.set_page_config(
    page_title="JAValorant movie search engine",
    layout="wide"
)

def create_filters():
    with st.sidebar:
        st.title("Filters")
        
        with st.expander("Genre"):
            selected_genres = st.multiselect("Choose genres", unique_genres)

        with st.expander("Language"):
            selected_languages = st.multiselect("Choose languages", unique_language)

        with st.expander("Production Country"):
            selected_countries = st.multiselect("Choose countries", unique_production_countries)

        with st.expander("Production Company"):
            selected_companies = st.multiselect("Choose companies", unique_production_companies)

        with st.expander("Collection"):
            selected_collections = st.multiselect("Choose collections", unique_belongs_to_collection)

    filters = {
        'genres': selected_genres,
        'languages': selected_languages,
        'countries': selected_countries,
        'companies': selected_companies,
        'collections': selected_collections
    }

    return filters

def display_movie_details(movie):
    st.title(movie['title'])
    # st.image(movie['poster_url'], width=500)
    st.write(movie['overview'])
    st.write("### Rating")
    st.write(movie['vote_average'])
    st.write("### Popularity")
    st.write(movie['popularity'])

def display_search_results(results, query):
    st.title(f"Search Results for your query:")
    
    if results.empty:
        st.write("No results found.")
        return

    for index, row in results.iterrows():
        st.subheader(row['title'])
        st.write(row['overview'])
        st.write(row['vote_average'])
        st.write(row['popularity'])
        st.image(row['poster_path'], width=200)

        if st.button("More Details", key=f"details-{index}"):
            display_movie_details(row)
            return

def main():
    st.title("JAValorant movie search engine")

    filters = create_filters()

    filter_query = " ".join([
        " ".join([f"+{genre.replace(' ', '_')}" for genre in filters['genres']]),
        " ".join([f"+{language.replace(' ', '_')}" for language in filters['languages']]),
        " ".join([f"+{country.replace(' ', '_')}" for country in filters['countries']]),
        " ".join([f"+{company.replace(' ', '_')}" for company in filters['companies']]),
        " ".join([f"+{collection.replace(' ', '_')}" for collection in filters['collections']])
    ])

    # Search bar
    query = st.text_input("Search for movies")
    combined_query = f"{query} {filter_query}".strip()
    if st.button("Search"):
        results = relevant_df(combined_query)
        display_search_results(results, combined_query)

main()