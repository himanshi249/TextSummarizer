# TextSummarizer
The Text Summarizer uses an Extractive Summarization
method which attempts to summarize articles by selecting a subset of words that retain the
most important points. Weights are assigned to the important part of sentences using this
approach which is then used to form the summary. We have used unsupervised
learning approach to find the sentences similarity and rank them. The general flow of the
code will be input article, split into sentences, remove stop words, build a similarity matrix,
generate a rank-based matrix, pick top N sentences for summary.
