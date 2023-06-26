import catalog_serach

# Search the catalog for "search_term"
results = catalog_classifier.search("catalog.db", "search_term")

# Print the results
for result in results:
    print(result)
