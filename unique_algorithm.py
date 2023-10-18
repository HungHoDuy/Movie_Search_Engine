import unique

unique_genres = unique.unique_genres

unique_language = unique.unique_language
unique_production_companies = unique.unique_production_companies
unique_production_countries = unique.unique_production_countries

unique_genres_read = [str(value).replace(' ','_') for value in unique_genres]
unique_language_read = [str(value).replace(' ','_') for value in unique_language]
unique_production_companies_read = [str(value).replace(' ','_') for value in unique_production_companies]
unique_production_countries_read = [str(value).replace('','_') for value in unique_production_countries]
