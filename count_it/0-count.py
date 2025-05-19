#!/usr/bin/python3
"""
This module contains a function to count keywords in the titles of
hot articles from a given Reddit subreddit.
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None,
                hot_list_counts=None, initial_word_freq_map=None):
    """
    Recursively queries the Reddit API for a given subreddit, counts
    occurrences of a list of keywords (case-insensitive) in the titles of
    hot articles, and prints the counts sorted.

    Args:
        subreddit (str): The subreddit to query (e.g., "programming").
        word_list (list): A list of keywords to count (e.g., ["python", "java"]).
        after (str, optional): The Reddit API 'after' parameter for pagination.
                               Defaults to None for the first call.
        hot_list_counts (dict, optional): A dictionary storing the raw counts of
                                          each keyword found in titles.
                                          Passed through recursive calls.
                                          Defaults to None for the first call.
        initial_word_freq_map (Counter, optional): A collections.Counter object
                                                   storing the frequency of each
                                                   (lowercase) keyword in the
                                                   initial `word_list`. Passed
                                                   through recursive calls.
                                                   Defaults to None for the first call.
    """

    # Initialize keyword tracking structures on the very first call
    if initial_word_freq_map is None:
        initial_word_freq_map = Counter()
        # Store unique lowercase keywords to initialize hot_list_counts
        unique_lower_keywords = set()
        for word in word_list:
            lw = word.lower()
            initial_word_freq_map[lw] += 1  # Count occurrences in input list
            unique_lower_keywords.add(lw)   # Track unique keywords

        # hot_list_counts will store raw occurrences of keywords from titles
        # This should also be initialized only on the first call
        if hot_list_counts is None:
            hot_list_counts = {key: 0 for key in unique_lower_keywords}

    # API request setup
    # Using a descriptive User-Agent is good practice for Reddit API
    headers = {'User-Agent': 'KeywordCounterBot/0.1 by T3Chat'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Parameters for the API request
    params = {'limit': 100}  # Request a larger number of items per page
    if after:
        params['after'] = after  # For pagination

    current_page_after_token = None  # To store 'after' token from current API response

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False) # Do not follow redirects

        # Check if the request was successful
        if response.status_code == 200:
            try:
                data = response.json()
                # Ensure data structure is as expected
                if 'data' in data and 'children' in data['data']:
                    posts = data['data']['children']
                    # Get the 'after' token for the next page
                    current_page_after_token = data['data'].get('after')

                    # Process titles from the current page
                    for post in posts:
                        title = post['data'].get('title', "")
                        # Tokenize title: lowercase and split by whitespace.
                        # This handles "java." vs "java" as per requirements.
                        title_tokens = title.lower().split()

                        # Count keywords
                        # hot_list_counts.keys() are the unique lowercase keywords
                        for keyword_to_find in hot_list_counts.keys():
                            for token_in_title in title_tokens:
                                if token_in_title == keyword_to_find:
                                    hot_list_counts[keyword_to_find] += 1
            except ValueError:  # JSONDecodeError
                # If JSON parsing fails, treat as no further data on this path
                current_page_after_token = None
        # If status_code is not 200 (e.g., 404, redirect),
        # current_page_after_token remains None, stopping recursion for this path.

    except requests.RequestException:
        # Network errors (timeout, connection error, etc.)
        # current_page_after_token remains None, stopping recursion for this path.
        pass # Fall through to the recursive call/print logic

    # Decide whether to recurse or print results
    if current_page_after_token is not None:
        # More pages to fetch, make a recursive call
        count_words(subreddit, word_list, current_page_after_token,
                    hot_list_counts, initial_word_freq_map)
    else:
        # Base case for recursion:
        # - No more pages (current_page_after_token is None).
        # - Or an error occurred (network, bad status, bad JSON),
        #   preventing further fetching.

        # Ensure keyword tracking structures are available (should be if first call ran)
        if initial_word_freq_map is None or hot_list_counts is None:
            return  # Should ideally not be hit in normal operation

        final_printable_results = {}
        for keyword, raw_title_count in hot_list_counts.items():
            # Only consider keywords that were actually found in titles
            if raw_title_count > 0:
                # Get the multiplier from the original word_list frequency
                original_list_multiplier = initial_word_freq_map.get(keyword, 0)
                
                if original_list_multiplier > 0:
                    final_count = raw_title_count * original_list_multiplier
                    # Ensure the final count is positive before adding
                    if final_count > 0:
                         final_printable_results[keyword] = final_count
        
        # If no keywords have positive counts, print nothing
        if not final_printable_results:
            return

        # Sort results:
        # 1. Primary key: count (descending)
        # 2. Secondary key: keyword (alphabetical ascending, A-Z)
        sorted_items = sorted(final_printable_results.items(),
                              key=lambda item: (-item[1], item[0]))

        # Print the sorted results
        for keyword_value, count_value in sorted_items:
            # Keywords are already lowercase from initial_word_freq_map keys
            print(f"{keyword_value}: {count_value}")
