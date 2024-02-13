# -------------------------------------------------------------------------
# AUTHOR: Dhruvi Choksi
# FILENAME: similarity.py
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# Importing some Python libraries
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Defining the documents
doc1 = "soccer is my favorite sport"
doc2 = "I like sports and my favorite one is soccer"
doc3 = "support soccer at the olympic games"
doc4 = "I do like soccer, my favorite sport in the olympic games"

# Use the following words as terms
terms = ['soccer', 'favorite', 'sport', 'like', 'one', 'support', 'olympic', 'games']

# create document-term matrix
document_term_matrix = np.array([
    [doc1.count(term) for term in terms],
    [doc2.count(term) for term in terms],
    [doc3.count(term) for term in terms],
    [doc4.count(term) for term in terms],
])

# Compare the pairwise cosine similarities and store the highest one
Cosine_Paireise_Similarity = cosine_similarity(document_term_matrix)
Highest_Similarity = np.argmax(Cosine_Paireise_Similarity - np.eye(Cosine_Paireise_Similarity.shape[0]))

# Print the highest cosine similarity following the information below
print(f"Highest cosine similarity: {Highest_Similarity}")
# The most similar documents are: doc1 and doc2 with cosine similarity = x

