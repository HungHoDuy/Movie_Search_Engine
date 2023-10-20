import streamlit as st
from relevant import relevant_df
from unique import unique_genres, unique_original_language, unique_production_companies, unique_belongs_to_collection, unique_production_countries, unique_spoken_languages
from cast import unique_cast
from director import unique_director
from keywords import unique_keywords
import data_filter
from rating import rating_df
from popularity import popularity_df
from AtoZ import AtoZ_df
from ZtoA import ZtoA_df
from streamlit_extras.app_logo import add_logo
from streamlit_modal import Modal

# Preconf
st.set_page_config(
    page_title="PyHub",
    layout="wide"
)

def create_filters():
    with st.sidebar:

        st.title("Filters")
        
        with st.expander("Genre"):
            selected_genres = st.multiselect("Choose genres", unique_genres)

        with st.expander("Language"):
            selected_languages = st.multiselect("Choose languages", unique_original_language)

        with st.expander("Production Country"):
            selected_countries = st.multiselect("Choose countries", unique_production_countries)

        with st.expander("Production Company"):
            selected_companies = st.multiselect("Choose companies", unique_production_companies)

        with st.expander("Collection"):
            selected_collections = st.multiselect("Choose collections", unique_belongs_to_collection)

        with st.expander("Spoken Language"):
            selected_spoken_languages = st.multiselect("Choose spoken languages", unique_spoken_languages)

        with st.expander("Cast"):
            selected_cast = st.multiselect("Choose cast", unique_cast)

        with st.expander("Director"):
            selected_director = st.multiselect("Choose director", unique_director)

        with st.expander("Keywords"):
            selected_keywords = st.multiselect("Choose keywords", unique_keywords)

    filters = {
        'genres': selected_genres,
        'languages': selected_languages,
        'countries': selected_countries,
        'companies': selected_companies,
        'collections': selected_collections,
        'spoken_languages': selected_spoken_languages,
        'cast': selected_cast,
        'director': selected_director,
        'keywords': selected_keywords
    }

    return filters

def display_search_results(results, query, results_limit=10):
    # st.title(f"Search Results for '{query}':")

    # if results.empty:
    #     st.write("No results found.")
    #     return

    # half_results_limit = results_limit // 2
    # cols_row1 = st.columns(half_results_limit)
    # cols_row2 = st.columns(half_results_limit)

    # for index, row in enumerate(results.head(results_limit).iterrows()):
    #     idx, data = row

    #     cols = cols_row1 if index < half_results_limit else cols_row2
    #     col = cols[index % half_results_limit]

    #     with col:
    #         poster_url = data['poster_path'] if data['poster_path'] else 'logo.png'
    #         col.image(poster_url, width=200)
    #         col.write(data['title'])

    #         modal_key = f"movie-detail-{index}" 
    #         modal = Modal("Movie Detail", key=modal_key)
    #         open_modal = col.button("More Details", key=f"open-{modal_key}")
    
    #         if open_modal:
    #             modal.open()

    #         if modal.is_open():
    #             with modal.container():
    #                 col.write(f"**Overview:** {data['overview']}")
    #                 col.write(f"**Genres:** {data['genres']}")
    #                 col.write(f"**Production Companies:** {data['production_companies']}")
    #                 col.write(f"**Cast:** {data['cast']}")
    #                 col.write(f"**Director:** {data['director']}")
    #                 col.write(f"**Keywords:** {data['keywords']}")

    for index, row in results.head(results_limit).iterrows():
        st.subheader(row['title'])
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(row['poster_path'], width=200)
        with col2:
            st.write(f"Genre: {row['genres']}")
            st.write(f"Overview: {row['overview']}")
            st.write(f"Production Companies: {row['production_companies']}")
            st.write(f"Vote Average: {row['vote_average']}")
            st.write(f"Popularity: {row['popularity']}")

        # if st.button("More Details", key=f"details-{index}"):
        #     display_movie_details(row)
        #     return

def main():
    st.image("logo.png")
    st.title("PyHub - Movie search engine")

    filters = create_filters()

    filter_query = " ".join([
        " ".join([f"+{genre.replace(' ', '_')}" for genre in filters['genres']]),
        " ".join([f"+{language.replace(' ', '_')}" for language in filters['languages']]),
        " ".join([f"+{country.replace(' ', '_')}" for country in filters['countries']]),
        " ".join([f"+{company.replace(' ', '_')}" for company in filters['companies']]),
        " ".join([f"+{collection.replace(' ', '_')}" for collection in filters['collections']]),
        " ".join([f"+{spoken_language.replace(' ', '_')}" for spoken_language in filters['spoken_languages']]),
        " ".join([f"+{cast.replace(' ', '_')}" for cast in filters['cast']]),
        " ".join([f"+{director.replace(' ', '_')}" for director in filters['director']]),
        " ".join([f"+{keyword.replace(' ', '_')}" for keyword in filters['keywords']]),
    ])

    # Search bar
    query = st.text_input("Search for movies")

    combined_query = f"{query} {filter_query}".strip()
    sort = st.selectbox("Sort by", ["Relevance", "Rating", "Popularity", "A to Z", "Z to A"])
    if st.button("Search"):
        wordfix = ' '.join(data_filter.Spell_fix(query))
        st.write(f"Showing results for: {wordfix}")
        st.write(f"Search instead for: {query}")

        if sort == "Relevance":
            results = relevant_df(combined_query)
        elif sort == "Rating":
            results = rating_df(combined_query)
        elif sort == "Popularity":
            results = popularity_df(combined_query)
        elif sort == "A to Z":
            results = AtoZ_df(combined_query)
        elif sort == "Z to A":
            results = ZtoA_df(combined_query)

        display_search_results(results, query)


main()