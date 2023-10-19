import unique

unique_genres = unique.unique_genres
unique_language = unique.unique_language
unique_language = [item.lower() for item in unique_language]
unique_production_companies = unique.unique_production_companies
unique_belongs_to_collection = unique.unique_belongs_to_collection
unique_production_countries = unique.unique_production_countries

unique_genres_read = [str(value).replace(' ','_') for value in unique_genres]
unique_language_read = [str(value).replace(' ','_') for value in unique_language]
unique_production_companies_read = [str(value).replace(' ','_') for value in unique_production_companies]
unique_belongs_to_collection_read = [str(value).replace(' ','_') for value in unique_belongs_to_collection]
unique_production_countries_read = [str(value).replace(' ','_') for value in unique_production_countries]