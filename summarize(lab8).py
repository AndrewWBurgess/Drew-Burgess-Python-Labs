#!/usr/bin/env python
"""summarize

Summarize a document using extractive text summarization via TF-IDF.

Usage:
  summarize.py [-o <file> | --output=<file>] [<input-file>]
  summarize.py (-h | --help)

Options:
  -h --help            Show this screen.
  -o --output=<file>   Write output to file instead of stdout.
"""
from docopt import docopt
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import sys
import math
from collections import defaultdict
from collections.abc import Callable
from typing import List, Dict, Callable

def load_document(textfile: str) -> List[str]:
    """Reads a text file and returns a list of sentences."""
    with open(textfile, 'r', encoding='utf-8') as f:
        text = f.read()
    sentences = sent_tokenize(text)
    return sentences

def clean_text(text: List[str]) -> List[List[str]]:
    """Transform text into a list of cleaned terms for each sentence.
    Each sentence is tokenized, lowercased, and stripped of non-alphanumeric terms."""
    sentences: List[List[str]] = []
    for line in text:
        cleaned_sentence = [word.casefold() for word in word_tokenize(line) if word.isalnum()]
        if cleaned_sentence:
            sentences.append(cleaned_sentence)
    return sentences

def calculate_tf(sentences: List[List[str]]) -> List[Dict[str, float]]:
    """Calculate Term Frequency for each sentence of the document.
    Returns a list where each index corresponds to a sentence, and each value is a dictionary of terms and their TF values."""
    tf_matrix: List[Dict[str, float]] = []
    for sentence in sentences:
        word_count = defaultdict(int)
        for word in sentence:
            word_count[word] += 1
        sentence_length = len(sentence)
        tf_dict = {word: count / sentence_length for word, count in word_count.items()}
        tf_matrix.append(tf_dict)
    return tf_matrix

def calculate_idf(sentences: List[List[str]]) -> Dict[str, float]:
    """Calculate the Inverse Document Frequency of each term.
    Returns a dictionary with terms as keys and their IDF values as values."""
    total_sentences = len(sentences)
    word_doc_count = defaultdict(int)
    for sentence in sentences:
        unique_words = set(sentence)
        for word in unique_words:
            word_doc_count[word] += 1
    idf_dict = {word: math.log(total_sentences / count) for word, count in word_doc_count.items()}
    return idf_dict

def score_sentences(tf_matrix: List[Dict[str, float]], idf_matrix: Dict[str, float], sentences: List[List[str]]) -> List[float]:
    """Score each sentence for importance based on the terms it contains.
    Returns a list where each index corresponds to a sentence, and each value is the sum of TF-IDF scores of each word in the sentence."""
    scores: List[float] = []
    for i, sentence in enumerate(sentences):
        sentence_score = 0.0
        for word in sentence:
            tf = tf_matrix[i].get(word, 0)
            idf = idf_matrix.get(word, 0)
            tf_idf = tf * idf
            sentence_score += tf_idf
        scores.append(sentence_score)
    return scores

def threshold_inclusion(text: List[str], scores: List[float], threshold: float = 1.0) -> List[str]:
    """Use a multiple of the average TF-IDF score as a threshold for inclusion in the summary."""
    avg_score = sum(scores) / len(scores)
    summary = []
    for index, score in enumerate(scores):
        if score >= threshold * avg_score:
            summary.append(text[index])
    return summary

def summarize(text: List[str], inclusion: Callable[[List[str], List[float]], List[str]]) -> str:
    """Summarizes a given text using TF-IDF and a given inclusion function."""
    sentences = clean_text(text)
    tf_matrix = calculate_tf(sentences)
    idf_matrix = calculate_idf(sentences)
    scores = score_sentences(tf_matrix, idf_matrix, sentences)
    summary_sentences = inclusion(text, scores)
    return ' '.join(summary_sentences) + '\n'

def main():
    nltk.download('punkt')

    arguments = docopt(__doc__)
    if arguments['<input-file>']:
        try:
            document = load_document(arguments['<input-file>'])
        except FileNotFoundError:
            print(f"Error: File {arguments['<input-file>']} not found.")
            sys.exit(1)
    else:
        # Read from stdin
        print("Enter the text to summarize (Ctrl+D to end):")
        document = sys.stdin.read()
        document = sent_tokenize(document)

    # Define inclusion function with threshold
    func = lambda text, scores: threshold_inclusion(text, scores, threshold=1.0)

    summary = summarize(document, func)

    if arguments['--output']:
        with open(arguments['--output'], 'w', encoding='utf-8') as outfile:
            outfile.write(summary)
    else:
        print("Summary:")
        print(summary)

if __name__ == '__main__':
    main()
