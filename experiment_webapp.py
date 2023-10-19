import streamlit as st
from streamlit_tailwind import st_tw

# Tailwind CSS card example
movie_card = """
    <div class="max-w-sm rounded overflow-hidden shadow-lg">
      <img class="w-full" src="https://source.unsplash.com/random/400x200" alt="Sunset in the mountains">
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">Movie Title</div>
        <p class="text-gray-700 text-base">
          Movie description goes here. This is a brief overview of the movie's plot, characters, and themes.
        </p>
      </div>
      <div class="px-6 pt-4 pb-2">
        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">#Action</span>
        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">#Adventure</span>
        <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700">#Fantasy</span>
      </div>
    </div>
"""

# Navigation bar
st.sidebar.title('Navigation')
selected_nav = st.sidebar.radio('Go to', ['Home', 'Movies', 'TV Shows', 'My List'])

# Featured Movie Section
st.title('Featured Movie')
st_tw(movie_card, height=400, key='featured')  # Adding a unique key

# Movies by Genre
st.title('Browse Movies by Genre')
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi']

for index, genre in enumerate(genres):
    st.subheader(genre)
    st_tw(movie_card, height=400, key=f'genre-{index}')  # Adding a unique key for each genre
    st.write("---")  # Add a separator

# Footer
st.write('---')
st.write('Netflix Clone with Streamlit and Tailwind CSS')
