# Blog Tagger 1.1.0
A simple Blog Tagging Engine in Python

06 May 2016

## Description

A simple Tagging Engine in Python which takes a user-specified plain text file (with or without punctuation), deals with
punctuation, strips out excluded/redundant words (per in-built and user-specified lists), counts and returns All or "Top n" words and their counts in descending order of frequency.

Includes options for user to:
* specify/save additional user-identified excluded words
* specify/save tags list as separate CSV file

Applications:
* highlighting top n words in a blog post (and returning a file of user-specifed tags)
* reviewing relevance of articles, web pages, etc. to a particular topic (and returning a file of user-specifed keywords)

Some problems to be ironed out:

    Most common punctuation marks are dealt with but need to add error-handling or user-specificaation for less common punctuation;
    Simple engine does not cope with phrases which legitimately includes both alpha-characters and punctuation (i.e. code);
    Words appearing both singular and plural currently returned as two unique words;
    Need to add better error-handling on various user inputs.

Further improvements to be made:

* Add option to deal with html-tagged text files;
* Add option to parse from a given URL;
* Add option to identify key phrases (pairs, triples, fours);
* Add ability to handle plurals and singulars as one word (at user request);
* Add better error-handling on various user inputs;
* Add ability to handle file paths (file in location other than working directory);
* Improve flexibility of saving outputs to file (incl. specify filepaths).

Future developments planned:

    Allow user to specify whether uploading simple text or html. If html, the program can use html tags (title, headers (h1, h2, etc.), strong or italic html tags to weight importance of text (either as words or phrases) more highly than normal, untagged/unformatted text. This will help make the program more useful if being used, for example, to auto-tag a Wordpress blog post;
    Review the text in pairs and/or triplets to identify significant phrases. User prompted to check/confirm if phrase is a significant phrase. User able to modify/overwrite significant phrase as required before appending to a list;
    The user can be prompted for a file path and filename where the significant phrases list can be saved. This can then be reloaded when using the program multiple times on multiple web pages/articles/etc;
    The same functionality can be used to test titles and headers for significant phrases.

This functionality will be useful for accelerated learning, and for rapid searching/reviewing of many web sites/pages/articles.
